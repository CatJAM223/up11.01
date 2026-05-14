from repositories.admin_repo import AdminRepository
from werkzeug.security import generate_password_hash
from flask import session, redirect, render_template, flash, url_for
from repositories.task_repo import TaskRepository

class AdminService:
    @staticmethod
    def create_default_admin(login='admin', password='admin123'):
        existing = AdminRepository.get_by_login(login)
        if not existing:
            hashed = generate_password_hash(password)
            return AdminRepository.create(login, hashed)
    
    @staticmethod
    def admin_panel():
        if session.get('role') != 'admin':
            flash('Доступ только для админа!', 'error')
            return redirect(url_for('index'))
    
        tasks = TaskRepository.get_all
        
        return render_template('admin_panel.html', tasks=tasks)