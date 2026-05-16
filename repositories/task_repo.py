from database.models import Task, db
from datetime import date
from sqlalchemy.exc import IntegrityError
from schemas.task_schemas import Task_Create, Task_Edit

class TaskRepository:
    @staticmethod
    def get_active():
        return Task.query.filter_by(is_active=True).filter(Task.worker_id.is_(None)).all()

    @staticmethod
    def get_by_id(task_id):
        return Task.query.get_or_404(task_id)
    
    @staticmethod
    def get_task_by_id(user_id):
        return Task.query.filter_by(worker_id=user_id, is_active=True).first()

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
    def apply(user_id, task_id):
        try:
            task = Task.query.filter_by(id=task_id, worker_id=None, is_active=True).first()
            if task:
                task.worker_id = user_id
                db.session.commit()
                return True, "Вы назначены на задачу!"
            return False, "Задача уже занята или неактивна"
        except IntegrityError:
            db.session.rollback()
            return False, "У вас уже есть активная задача! Нельзя откликнуться на несколько задач."
        except Exception as e:
            db.session.rollback()
            return False, f"Ошибка: {str(e)}"