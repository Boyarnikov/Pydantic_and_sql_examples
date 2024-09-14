from typing import Self
from datetime import date
from uuid import UUID, uuid4
from enum import Enum
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    field_validator,
    model_validator,
)

class Department(Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"

class Employee(BaseModel):
    employee_id: UUID = Field(default_factory=uuid4, frozen=True)
    name: str = Field(min_length=1, frozen=True)
    email: EmailStr = Field(pattern=r".+@example\.com$")
    salary: float = Field(alias="compensation", gt=0, repr=False)
    department: Department
    elected_benefits: bool

    @model_validator(mode="after")
    def check_it_benefits(self) -> Self:
        department = self.department
        elected_benefits = self.elected_benefits

        if department == Department.IT and elected_benefits:
            raise ValueError(
                "IT employees are contractors and don't qualify for benefits"
            )
        return self


new_employee = {
     "name": "Alexis Tau",
     "email": "ataue@example.com",
     "compensation": 100_000,
     "department": "HR",
     "elected_benefits": True,
}

Employee.model_validate(new_employee)