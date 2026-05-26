from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum


class EmployeeStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    ON_LEAVE = "On Leave"


class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    department: str
    designation: str
    status: EmployeeStatus = EmployeeStatus.ACTIVE
    date_of_joining: str
    salary: Optional[float] = None
    avatar: Optional[str] = None


class EmployeeResponse(EmployeeBase):
    id: int

    class Config:
        from_attributes = True


class EmployeeListResponse(BaseModel):
    total: int
    employees: list[EmployeeResponse]


class ErrorResponse(BaseModel):
    detail: str
