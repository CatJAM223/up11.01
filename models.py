from peewee import *

db = SqliteDatabase('models.db')

class BaseModel(Model):
    class Meta():
        database = db
        
class User(BaseModel):
    login = CharField()
    password = CharField()
    
class Admin(BaseModel):
    login = CharField()
    password = CharField()
    
class Task(BaseModel):
    name = CharField()
    description = TextField()
    data = DateField()
    is_active = BooleanField(default=False)
    
if __name__ == '__main__':
    db.create_tables([User, Admin, Task])