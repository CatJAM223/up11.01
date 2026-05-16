from pydantic import BaseModel, Field, field_validator

class Admin_Valid(BaseModel):
    login: str
    password: str