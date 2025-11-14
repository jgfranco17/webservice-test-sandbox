from pydantic import BaseModel


class SumRequest(BaseModel):
    numbers: list[int]
