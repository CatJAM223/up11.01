from flask import render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from database.models import Admin, Users, Task


def apply_task(task_id):
    if session.get('role') == 'admin':
        flash('Админ не может откликаться!', 'error')
        return redirect(url_for('admin_panel'))
    

        flash(f'Отклик на "{task.name}" принят!', 'success')
    else:
        flash('Задача уже занята!', 'error')
    return redirect(url_for('main'))

def index():
    if session.get('role') == 'admin':
        return redirect(url_for('admin_panel'))
    
    tasks = Task.query.filter_by(is_active=True).filter(Task.worker_id.is_(None)).all()
    return render_template('user_tasks.html', tasks=tasks)

def task_edit(task_id):
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
        
       
        flash('Задача обновлена!', 'success')
        return redirect(url_for('admin_panel'))
    
    return render_template('task_form.html', task=task)



