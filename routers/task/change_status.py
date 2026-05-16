from flask import session, url_for, redirect, flash
from repositories.task_repo import TaskRepository
from . import tasks_bp

@tasks_bp.route('/<int:task_id>/deactivate', methods=['POST'])
def deactivate(task_id):
    if session.get('role') != 'admin':
        flash('Доступ только для админа!', 'error')
        return redirect(url_for('auth.login'))
    
    task = TaskRepository.deactive(task_id)
    
    flash(f'Задача "{task.name}" деактивирована', 'warning')
    return redirect(url_for('admin.admin_panel'))

@tasks_bp.route('/<int:task_id>/activate', methods=['POST'])
def activate(task_id):
    if session.get('role') != 'admin':
        flash('Доступ только для админа!', 'error')
        return redirect(url_for('auth.login'))
    
    task = TaskRepository.activite(task_id)
    
    flash(f'Задача "{task.name}" активирована', 'success')
    return redirect(url_for('admin.admin_panel'))