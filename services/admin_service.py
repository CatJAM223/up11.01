from repositories.admin_repo import AdminRepository
from werkzeug.security import generate_password_hash

class AdminService:
    @staticmethod
    def create_default_admin(login='admin', password='admin123'):
        existing = AdminRepository.get_by_login(login)
        if not existing:
            hashed = generate_password_hash(password)
            return AdminRepository.create(login, hashed)