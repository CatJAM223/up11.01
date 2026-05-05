from config import create_app
from flask import render_template, request, redirect, url_for
from database.models import Admin, db
from werkzeug.security import generate_password_hash

def init_db():
    app = create_app()
    with app.app_context():
        db.create_all()
        existing_admin = Admin.query.filter_by(login='admin').first()
        if not existing_admin:
            admin = Admin(
                login='admin',
                password=generate_password_hash('admin123')
            )
            db.session.add(admin)
            db.session.commit()
            
def index():
    return render_template('index.html')
        
def admin_panel():
    return render_template('admin_panel.html')

def task_create():
    return render_template('task_form.html', task_id=None)

def task_edit(task_id):
    return render_template('task_form.html', task_id=task_id)

def task_save():
    title = request.form.get('title')
    description = request.form.get('description')
    is_active = request.form.get('is_active') == 'on'
    print(f"[ЗАГЛУШКА] Сохранение задачи: {title}, активна: {is_active}")
    return redirect(url_for('admin_panel'))

def apply_task(task_id):
    return render_template('apply_success.html', task_id=task_id)