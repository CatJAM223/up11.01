from flask import request, session, flash, url_for, redirect, render_template
from repositories.task_repo import TaskRepository
from schemas.task_schemas import Task_Edit
from . import tasks_bp

@tasks_bp.route('/<int:task_id>/edit', methods=['GET', 'POST'])
def edit(task_id):
    if session.get('role') != 'admin':
        flash('Доступ только для админа!', 'error')
        return redirect(url_for('main'))
    
    if request.method == 'POST':
        deadline_str = request.form.get('deadline')
        deadline = None
        if deadline_str:
            from datetime import datetime
            try:
                deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()
            except ValueError:
                flash('Неверный формат даты!', 'error')
                return redirect(url_for('task_edit', task_id=task_id))

        task_data = Task_Edit(
            id=task_id,
            name=request.form.get('name'),
            description=request.form.get('description'),
            deadline=deadline
        )

        task = TaskRepository.edit(task_data)
        
        flash('Задача обновлена!', 'success')
        return redirect(url_for('admin.admin_panel'))
    
    task = TaskRepository.get_by_id(task_id)
    return render_template('task_form.html', task=task)