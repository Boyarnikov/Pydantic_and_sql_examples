from datetime import date
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, EmailStr


class Department(Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"


class Employee(BaseModel):
    employee_id: UUID = uuid4()
    name: str
    email: EmailStr
    date_of_birth: date
    salary: float
    department: Department
    elected_benefits: bool


print(
    Employee(
        name="Chris DeTuma",
        email="cdetuma@example.com",
        date_of_birth="1998-04-02",
        salary=123_000.00,
        department="IT",
        elected_benefits=True,
    ).model_dump()
)

print(
    Employee(
        name="Chris DeTuma2",
        email="cdetuma@example.com",
        date_of_birth="1998-04-02",
        salary=123_000.00,
        department="IT",
        elected_benefits=True,
    ).model_dump()
)

try:
    Employee(
        employee_id="123",
        name=False,
        email="cdetumaexamplecom",
        date_of_birth="1939804-02",
        salary="high paying",
        department="PRODUCT",
        elected_benefits=300)
except ValueError as e:
    print(e)


"""
{'$defs': 
    {
    'Department': {'enum': ['HR', 'SALES', 'IT', 'ENGINEERING'],
    'title': 'Department', 'type': 'string'}},
    'properties':
        {'employee_id':
         {'default': 'f20dd7a4-bf00-454a-a5c4-31756f272946',
          'format': 'uuid',
           'title': 'Employee Id',
            'type': 'string'},
    'name': {'title': 'Name', 'type': 'string'},
    'email': {'format': 'email', 'title': 'Email', 'type': 'string'},
    'date_of_birth': {'format': 'date', 'title': 'Date Of Birth', 'type': 'string'},
    'salary': {'title': 'Salary', 'type': 'number'},
    'department': {'$ref': '#/$defs/Department'}, 'elected_benefits': {'title': 'Elected Benefits', 'type': 'boolean'}}, 'required': ['name', 'email', 'date_of_birth', 'salary', 'department', 'elected_benefits'],
    'title': 'Employee',
    'type': 'object'}
"""