from flask import session, url_for, redirect, render_template
from repositories.task_repo import TaskRepository
from . import tasks_bp

@tasks_bp.route('/my_task')
def my_task():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    
    my_task = TaskRepository.get_task_by_id(user_id)
    return render_template('my_task.html', task=my_task)