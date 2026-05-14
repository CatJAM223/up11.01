from config import db
from database.models import Admin

class AdminRepository:
    @staticmethod
    def get_by_login(login: str):
        return Admin.query.filter_by(login=login).first()