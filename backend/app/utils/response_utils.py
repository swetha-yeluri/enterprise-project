from typing import Any, Optional
from fastapi.responses import JSONResponse


def success_response(data: Any, message: str = "Success", status_code: int = 200) -> JSONResponse:
    """
    Return a standardised success JSON response.

    Args:
        data: The payload to return.
        message: A human-readable success message.
        status_code: HTTP status code (default 200).
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "success",
            "message": message,
            "data": data,
        },
    )


def error_response(detail: str, status_code: int = 400) -> JSONResponse:
    """
    Return a standardised error JSON response.

    Args:
        detail: A human-readable error description.
        status_code: HTTP status code (default 400).
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "error",
            "message": detail,
            "data": None,
        },
    )
