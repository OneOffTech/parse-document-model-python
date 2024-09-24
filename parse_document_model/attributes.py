from abc import ABC
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class BoundingBox(BaseModel):
    min_x: float
    min_y: float
    max_x: float
    max_y: float
    page: int


class Attributes(BaseModel, ABC):
    pass


class DocumentAttributes(Attributes):
    pass


class PageAttributes(Attributes):
    page: int


class TextAttributes(Attributes):
    bounding_box: list[BoundingBox] = []
    level: Optional[int] = Field(None, gw=1, le=4)

    @field_validator('level')
    @classmethod
    def check_level(cls, v) -> int:
        if v is not None and v not in range(1, 5):
            raise ValueError("Level must be between 1 and 4 or None")
        return v