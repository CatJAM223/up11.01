from flask import Blueprint, session, render_template, redirect, url_for, flash
from repositories.task_repo import TaskRepository

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def admin_panel():
    if session.get('role') != 'admin':
        flash('Доступ только для админа!', 'error')
        return redirect(url_for('user.main'))
    
    tasks = TaskRepository.get_all()
        
    return render_template('admin_panel.html', tasks=tasks)