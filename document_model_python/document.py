from abc import ABC
from typing import List, Any, Optional

from pydantic import BaseModel, Field

from document_model_python.attributes import Attributes, PageAttributes, LeafAttributes
from document_model_python.marks import Mark


class Node(BaseModel, ABC):
    """Base element of a document.

    A document is a hierarchy of nodes.
    Nodes could represent: document, pages, headings, etc.
    """
    category: str = Field(
        title="Node Type",
        description="The type of node. Examples are: `doc`, `page`, `heading`, `body`, etc. For an exhaustive list "
                    "refers to the documentation.",
    )
    attributes: Optional[Attributes] = Field(
        title="Node Attributes",
        description="Attributes related to the node. An example is the reference page."
    )
    content: Any = Field(
        title="Node Content",
        description="The content of the node. If it is a leaf node this is text, otherwise it could be a list of "
                    "nodes.",
    )


class Leaf(Node):
    """The leaf node of a document.

    That's where the actual text is.

    """
    attributes: LeafAttributes = LeafAttributes()
    content: str
    marks: list[Mark] = []


class Page(Node):
    """The node that represents a document's page."""
    category: str = "page"
    attributes: PageAttributes
    content = list[Leaf]


class Document(Node):
    """The root node of a document."""
    category: str = "doc"
    attributes: Optional[Attributes] = None
    content: list[Page]
