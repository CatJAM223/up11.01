from config import create_app
from database.models import db
from services.admin_service import AdminService
from repositories.admin_repo import AdminRepository

def init_database():
    app = create_app()
    with app.app_context():
        db.create_all()
        admin = AdminRepository.get_by_login('admin')
        if not admin:
            AdminService.create_default_admin()
        
if __name__ == '__main__':
    init_database()