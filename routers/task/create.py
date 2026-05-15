from flask import request, session, flash, url_for, redirect, render_template
from repositories.task_repo import TaskRepository
from datetime import datetime
from schemas.task_schemas import Task_Create
from . import tasks_bp

@tasks_bp.route('/create', methods=['GET', 'POST'])
def create():
    if session.get('role') != 'admin':
        flash('Доступ только для админа!', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        deadline_str = request.form.get('deadline')
        deadline = None
        
        if deadline_str:
            try:
                deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()
            except ValueError:
                flash('Неверный формат даты!', 'error')
                return redirect(url_for('task_create'))

        task_data = Task_Create(
            name=request.form.get('name'),
            description=request.form.get('description'),
            deadline=deadline
        )

        task = TaskRepository.create(task_data)
        
        flash('Задача создана!', 'success')
        return redirect(url_for('admin.admin_panel'))
    
    return render_template('task_form.html', task = None)