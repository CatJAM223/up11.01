from repositories.user_repo import UserRepository
from werkzeug.security import generate_password_hash

class UserService:
    @staticmethod
    def register_user(name: str, login: str, password: str):
        existing = UserRepository.get_by_login(login)
        if existing:
            return None
        
        hashed_password = generate_password_hash(password)

        user = UserRepository.create(name, login, hashed_password)

        return user