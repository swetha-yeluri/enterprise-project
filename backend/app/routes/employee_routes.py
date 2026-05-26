from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from app.controllers.employee_controller import (
    get_all_employees,
    get_employee_by_id,
    get_department_summary,
    get_status_summary,
)
from app.models.employee_model import EmployeeListResponse, EmployeeResponse

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get("", response_model=EmployeeListResponse, summary="Get all employees")
def list_employees(
    department: Optional[str] = Query(None, description="Filter by department"),
    status: Optional[str] = Query(None, description="Filter by status (Active, Inactive, On Leave)"),
    search: Optional[str] = Query(None, description="Search by name or email"),
):
    """
    Retrieve all employees. Supports optional filtering by:
    - **department**: e.g. Engineering, HR
    - **status**: Active | Inactive | On Leave
    - **search**: partial match on first name, last name, or email
    """
    data = get_all_employees(department=department, status=status, search=search)
    return data


@router.get("/departments/summary", summary="Department summary")
def department_summary():
    """
    Returns the count of employees per department.
    """
    return get_department_summary()


@router.get("/status/summary", summary="Status summary")
def status_summary():
    """
    Returns the count of employees grouped by status.
    """
    return get_status_summary()


@router.get("/{employee_id}", response_model=EmployeeResponse, summary="Get employee by ID")
def retrieve_employee(employee_id: int):
    """
    Retrieve a single employee record by their unique ID.
    Returns **404** if the employee is not found.
    """
    employee = get_employee_by_id(employee_id)
    if not employee:
        raise HTTPException(
            status_code=404,
            detail=f"Employee with ID {employee_id} not found.",
        )
    return employee
