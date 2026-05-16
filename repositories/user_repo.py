from database.models import Users, db

class UserRepository:
    @staticmethod
    def get_by_login(login: str):
        return Users.query.filter_by(login=login).first()
    
    @staticmethod
    def create(name:str, login:str, password: str):
        user = Users(name=name, login=login, password=password)
        db.session.add(user)
        db.session.commit()
        return user