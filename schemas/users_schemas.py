from pydantic import BaseModel, Field, field_validator

class User_Valid(BaseModel):
    name: str
    login: str
    password: str