from config import db
from database.models import Admin

class AdminRepository:
    @staticmethod
    def get_by_login(login: str):
        return Admin.query.filter_by(login=login).first()

    @staticmethod
    def create(login: str, password: str):
        admin = Admin(login=login, password=password)
        db.session.add(admin)
        db.session.commit()
        return admin