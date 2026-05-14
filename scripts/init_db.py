from config import create_app, db

def init_database():
    app = create_app()
    with app.app_context():
        db.create_all()
        
if __name__ == '__main__':
    init_database()