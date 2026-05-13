from config import create_app, db
from flask import render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from database.models import Admin, Users, Task

def init_db():
    app = create_app()
    with app.app_context():
        db.create_all()

def register():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        
        if not name or not login or not password:
            flash('Заполните все поля!', 'error')
            return redirect(url_for('register'))
        
        if Users.query.filter_by(login=login).first():
            flash('Логин уже существует!', 'error')
            return redirect(url_for('register'))
        
        
        flash('Регистрация успешна! Войдите.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        role = request.form.get('role')
        
        if role == 'admin':
            admin = Admin.query.filter_by(login=login).first()
            if admin and check_password_hash(admin.password, password):
                session['user_id'] = admin.id
                session['role'] = 'admin'
                return redirect(url_for('admin_panel'))
            flash('Неверные данные админа!', 'error')
        else:
            user = Users.query.filter_by(login=login).first()
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                session['role'] = 'user'
                return redirect(url_for('main'))  # ← ИСПРАВЛЕНО!
            flash('Неверный логин или пароль!', 'error')
    
    return render_template('login.html')

def logout():
    session.clear()
    flash('Вы вышли', 'info')
    return redirect(url_for('login'))

# ============= ПОЛЬЗОВАТЕЛЬ =============

def apply_task(task_id):
    if session.get('role') == 'admin':
        flash('Админ не может откликаться!', 'error')
        return redirect(url_for('admin_panel'))
    
    task = Task.query.get_or_404(task_id)
    if task.is_active and task.worker_id is None:
        task.worker_id = session['user_id']
        db.session.commit()
        flash(f'Отклик на "{task.name}" принят!', 'success')
    else:
        flash('Задача уже занята!', 'error')
    return redirect(url_for('main'))  # ← ИСПРАВЛЕНО!

def index():
    if session.get('role') == 'admin':
        return redirect(url_for('admin_panel'))
    
    tasks = Task.query.filter_by(is_active=True).filter(Task.worker_id.is_(None)).all()
    return render_template('user_tasks.html', tasks=tasks)

# ============= АДМИН =============

def admin_panel():
    if session.get('role') != 'admin':
        flash('Доступ только для админа!', 'error')
        return redirect(url_for('index'))
    
    tasks = Task.query.all()
    return render_template('admin_panel.html', tasks=tasks)

def task_create():
    if session.get('role') != 'admin':
        flash('Доступ только для админа!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        # Преобразуем deadline из строки в date объект
        deadline_str = request.form.get('deadline')
        deadline = None
        if deadline_str:
            from datetime import datetime
            deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()
        
        task = Task(
            name=request.form.get('name'),
            description=request.form.get('description'),
            date=date.today(),
            deadline=deadline,
            is_active=request.form.get('is_active') == 'on'
        )
        db.session.add(task)
        db.session.commit()
        flash('Задача создана!', 'success')
        return redirect(url_for('admin_panel'))
    
    return render_template('task_form.html', task=None)

def task_edit(task_id):
    if session.get('role') != 'admin':
        flash('Доступ только для админа!', 'error')
        return redirect(url_for('index'))
    
    task = Task.query.get_or_404(task_id)
    
    if request.method == 'POST':
        # Преобразуем deadline из строки в date объект
        deadline_str = request.form.get('deadline')
        deadline = None
        if deadline_str:
            from datetime import datetime
            deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()
        
        task.name = request.form.get('name')
        task.description = request.form.get('description')
        task.deadline = deadline
        task.is_active = request.form.get('is_active') == 'on'
        db.session.commit()
        flash('Задача обновлена!', 'success')
        return redirect(url_for('admin_panel'))
    
    return render_template('task_form.html', task=task)

def task_save():
    # Старая заглушка, но уже не нужна, оставил для совместимости
    return redirect(url_for('admin_panel'))

def task_deactivate(task_id):
    if session.get('role') != 'admin':
        flash('Доступ только для админа!', 'error')
        return redirect(url_for('index'))
    
    task = Task.query.get_or_404(task_id)
    task.is_active = False
    db.session.commit()
    flash(f'Задача "{task.name}" деактивирована', 'warning')
    return redirect(url_for('admin_panel'))

def task_activate(task_id):
    if session.get('role') != 'admin':
        flash('Доступ только для админа!', 'error')
        return redirect(url_for('index'))
    
    task = Task.query.get_or_404(task_id)
    task.is_active = True
    db.session.commit()
    flash(f'Задача "{task.name}" активирована', 'success')
    return redirect(url_for('admin_panel'))

def task_delete(task_id):
    if session.get('role') != 'admin':
        flash('Доступ только для админа!', 'error')
        return redirect(url_for('index'))
    
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash(f'Задача "{task.name}" удалена из БД!', 'danger')
    return redirect(url_for('admin_panel'))