from database.models import Task, db
from datetime import date
from schemas.task_schemas import Task_Create, Task_Edit

class TaskRepository:
    @staticmethod
    def get_active():
        return Task.query.filter_by(is_active=True).filter(Task.worker_id.is_(None)).all()

    @staticmethod
    def get_by_id(task_id):
        return Task.query.get_or_404(task_id)

    @staticmethod
    def get_all():
        task = Task.query.all()
        return task
    
    @staticmethod
    def create(Tasks: Task_Create):
        task = Task(
            name=Tasks.name,
            description=Tasks.description,
            date_task=date.today(),
            deadline=Tasks.deadline
        )
        db.session.add(task)
        db.session.commit()
        return task
    
    @staticmethod
    def edit(Tasks: Task_Edit):
        task = Task.query.get_or_404(Tasks.id)
        if Tasks.name:
            task.name = Tasks.name
        if Tasks.description is not None:
            task.description = Tasks.description
        if Tasks.deadline:
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
            return task
        else:
            False