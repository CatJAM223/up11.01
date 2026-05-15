from repositories.task_repo import TaskRepository
from flask import session, flash, redirect, url_for
from database.models import db
from . import tasks_bp

@tasks_bp.route('/<int:task_id>/apply', methods=['POST'])
def apply(task_id):
    if session.get('role') != 'user':
        flash('Только пользователи могут откликаться!', 'error')
        return redirect(url_for('auth.login'))
    task = TaskRepository.apply(task_id)
    if task:
        task.worker_id = session.get('user_id')
        db.session.commit()
        flash('Вы назначены на задачу!', 'success')
    else:
        flash('Задача уже занята или неактивна', 'error')
    return redirect(url_for('user.view'))