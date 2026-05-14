from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import Optional

class Task_Create(BaseModel):
    name: str
    description: str 
    deadline: date
    
    @field_validator('deadline')
    def deadline_not_past(cls, v):
        if v < date.today():
            raise ValueError('Дедлайн не может быть в прошлом')
        return v

    
class Task_Edit(BaseModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    deadline: Optional[date]
    
class Task_Status(BaseModel):
    id: int
    is_active: Optional[bool]