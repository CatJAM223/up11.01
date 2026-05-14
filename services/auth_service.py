# services/auth_service.py
from repositories.admin_repo import AdminRepository
from repositories.user_repo import UserRepository
from werkzeug.security import check_password_hash

class AuthService:
    @staticmethod
    def authenticate(login: str, password: str, role: str):
        if role == 'admin':
            admin = AdminRepository.get_by_login(login)
            if admin and check_password_hash(admin.password, password):
                return admin, None
            return None, "Неверные данные админа!"
        else:
            user = UserRepository.get_by_login(login)
            if user and check_password_hash(user.password, password):
                return user, None
            return None, "Неверный логин или пароль!"