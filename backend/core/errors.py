from dataclasses import asdict, dataclass


@dataclass
class ErrorResponse:
    """Standard error response structure."""

    message: str
    solution: str


def new_error_response(message: str, solution: str | None = None) -> dict[str, str]:
    """Create a new ErrorResponse instance."""
    default_solution = "Please refer to the endpoint documentation for usage details"
    if solution is None:
        solution = default_solution
    response = ErrorResponse(message=message, solution=solution)
    return asdict(response)
