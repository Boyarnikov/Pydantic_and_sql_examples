from pydantic import BaseModel, EmailStr, constr


class User(BaseModel):
    name: constr(min_length=1, max_length=100)
    email: EmailStr
    age: int
    address: constr(max_length=255)
