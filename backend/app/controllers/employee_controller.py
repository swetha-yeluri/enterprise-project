from typing import List, Optional, Dict, Any
from app.database.mock_data import EMPLOYEES


def get_all_employees(
    department: Optional[str] = None,
    status: Optional[str] = None,
    search: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Retrieve all employees with optional filtering.

    Args:
        department: Filter by department name (case-insensitive).
        status: Filter by employee status.
        search: Search by first name, last name, or email.

    Returns:
        Dictionary with total count and filtered employee list.
    """
    result: List[Dict[str, Any]] = EMPLOYEES.copy()

    if department:
        result = [
            emp for emp in result
            if emp["department"].lower() == department.lower()
        ]

    if status:
        result = [
            emp for emp in result
            if emp["status"].lower() == status.lower()
        ]

    if search:
        search_lower = search.lower()
        result = [
            emp for emp in result
            if search_lower in emp["first_name"].lower()
            or search_lower in emp["last_name"].lower()
            or search_lower in emp["email"].lower()
        ]

    return {"total": len(result), "employees": result}


def get_employee_by_id(employee_id: int) -> Optional[Dict[str, Any]]:
    """
    Retrieve a single employee by their ID.

    Args:
        employee_id: The unique identifier of the employee.

    Returns:
        Employee dictionary if found, else None.
    """
    for employee in EMPLOYEES:
        if employee["id"] == employee_id:
            return employee
    return None


def get_department_summary() -> List[Dict[str, Any]]:
    """
    Return a summary of employee counts grouped by department.

    Returns:
        List of dictionaries with department name and employee count.
    """
    department_map: Dict[str, int] = {}

    for emp in EMPLOYEES:
        dept = emp["department"]
        department_map[dept] = department_map.get(dept, 0) + 1

    return [
        {"department": dept, "count": count}
        for dept, count in sorted(department_map.items())
    ]


def get_status_summary() -> Dict[str, int]:
    """
    Return a count of employees grouped by status.

    Returns:
        Dictionary mapping status labels to their counts.
    """
    summary: Dict[str, int] = {}

    for emp in EMPLOYEES:
        status = emp["status"]
        summary[status] = summary.get(status, 0) + 1

    return summary
