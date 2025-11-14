import logging
from http import HTTPStatus
from time import sleep

from fastapi import APIRouter, HTTPException

from backend.core.errors import new_error_response
from backend.core.types import StandardJsonResponse
from backend.routes.v0.models import SumRequest

logger = logging.getLogger(__name__)
simple_routes = APIRouter(prefix="/simple", tags=["SIMPLE"])


@simple_routes.post("/add", status_code=HTTPStatus.OK)
def add_numbers(request: SumRequest) -> StandardJsonResponse:
    """Add list of numbers and return the result.

    Args:
        request (SumRequest): JSON request body containing list of numbers.

    Raises:
        HTTPException: Raised when the input list is empty.

    Returns:
        StandardJsonResponse: JSON response containing the sum of the numbers.
    """
    if len(request.numbers) < 1:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=new_error_response(
                message="No numbers provided to add.",
                solution="Include at least one number in the 'numbers' list.",
            ),
        )
    result = sum(request.numbers)
    logger.debug(f"Adding {len(request.numbers)} numbers = {result}")
    return {"sum": result}


@simple_routes.get("/delay", status_code=HTTPStatus.OK)
def delayed_response(seconds: int = 1) -> StandardJsonResponse:
    """Return a response after a delay.

    Args:
        seconds (int, optional): Number of seconds to delay the response. Defaults to 1.

    Returns:
        StandardJsonResponse: JSON response indicating the delay duration.
    """
    logger.debug(f"Delaying response for {seconds} seconds")
    sleep(seconds)
    return {"message": f"Response delayed by {seconds} seconds"}
