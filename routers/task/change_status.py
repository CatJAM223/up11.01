from flask import session, url_for, redirect, flash
from repositories.task_repo import TaskRepository


def task_deactivate(task_id):
    if session.get('role') != 'admin':
        flash('Доступ только для админа!', 'error')
        return redirect(url_for('index'))
    
    task = TaskRepository.deactive
    
    flash(f'Задача "{task.name}" деактивирована', 'warning')
    return redirect(url_for('admin_panel'))

def task_activate(task_id):
    if session.get('role') != 'admin':
        flash('Доступ только для админа!', 'error')
        return redirect(url_for('index'))
    
    task = TaskRepository.activite
    
    flash(f'Задача "{task.name}" активирована', 'success')
    return redirect(url_for('admin_panel'))