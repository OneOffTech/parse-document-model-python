from typing import List, Union, TypedDict

from pydantic import BaseModel, Field

from document_model_python.marks import Mark, TextStyleMark


class BoundingBox(TypedDict):
    min_x: float
    min_y: float
    max_x: float
    max_y: float
    page: int


class ContentAttributes(BaseModel):
    bounding_box: List[BoundingBox] = []


class Content(BaseModel):
    role: str
    text: str
    marks: List[Union[Mark, TextStyleMark]] = []
    attributes: ContentAttributes = ContentAttributes()


class NodeAttributes(BaseModel):
    page: int


class Node(BaseModel):
    category: str
    attributes: NodeAttributes
    content: List[Content]
