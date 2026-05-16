from flask import redirect, url_for, session, render_template, Blueprint
from repositories.task_repo import TaskRepository

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def view():
    if session.get('role') == 'admin':
        return redirect(url_for('admin.admin_panel'))
    
    tasks = TaskRepository.get_active()
    return render_template('user_tasks.html', tasks=tasks)
