from database.models import Task, db
from datetime import datetime, date
from schemas.task_schemas import Task_Create, Task_Edit
from flask import session

class TaskRepository:
    @staticmethod
    def get_all():
        task = Task.query.all()
        return task
    
    @staticmethod
    def create(Tasks: Task_Create):
        task = Task(
            name=Tasks.name,
            description=Tasks.description,
            date=date.today(),
            deadline=Tasks.deadline
        )
        db.session.add(task)
        db.session.commit()
        return task
    
    @staticmethod
    def edit(Tasks: Task_Edit):
        task = Task.query.get_or_404(Tasks.id)
        task.name = Tasks.name
        task.description = Tasks.description
        task.deadline = Tasks.deadline
        db.session.commit()
        return task
        
    @staticmethod
    def deactive(task_id):
        task = Task.query.get_or_404(task_id)
        task.is_active = False
        db.session.commit()
        return task
    
    @staticmethod
    def activite(task_id):
        task = Task.query.get_or_404(task_id)
        task.is_active = True
        db.session.commit()
        return task

    @staticmethod
    def apply(task_id):
        task = Task.query.get_or_404(task_id)
        if task.is_active and task.worker_id is None:
            task.worker_id = session['user_id']
            db.session.commit()
            return task
        else:
            False