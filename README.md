![pypi](https://img.shields.io/pypi/v/document-model-python.svg)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://docs.pydantic.dev/latest/contributing/#badges)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

# :card_file_box: Document Model Python

**Document Model Python** is a library for representing text documents using a hierarchical model. 
This library allows you to define documents as a collection of nodes where each node can represent a document, page, 
text, heading, body, and more.

## 🌟 Key Features

- **Hierarchical Structure**: The document is modeled as a hierarchy of nodes. Each node could represent a part of the 
document such as a document itself, pages, text.
- **Rich Text Support**: Nodes can represent not only the content but also the marks (e.g., bold, italic) applied to 
the text.
- **Attributes**: Every node can have attributes that provide additional information such as page number, 
bounding box, etc.
- **Easy-to-use**: Built with [`Pydantic`](https://docs.pydantic.dev/latest/), ensures type validation and effortless 
creation of complex document structures.

## 📚 Structure Overview

### 1. **Node** (Base Class)

The base element of the document is a `Node`. This is the abstract class from which all other nodes inherit. 
Each node has:
- `category`: The type of the node (e.g., `doc`, `page`, `heading`).
- `attributes`: Optional field to attach extra data to a node.

### 2. **StructuredNode**

This extends the `Node` class and can contain other nodes as content. It is used for non-leaf nodes like 
`Document` and `Page`.

### 3. **Text**

This is a leaf node and contains the actual text content:

- `content`: The main text content.
- `marks`: List of text marks like bold, italic, text style, etc.
- `text`: Deprecated field, use `content` instead.
- `role`: Deprecated field, use `category` instead.

### 4. **Page**

Represents a page in the document:

- `category`: Always set to `"page"`.
- `attributes`: Can contain metadata like page number.
- `content`: List of `Text` nodes on the page.

### 5. **Document**

This is the root node of the document:

- `category`: Always set to `"doc"`.
- `attributes`: Document-wide attributes can be set here.
- `content`: List of `Page` nodes that form the document.

## 🖋️ Marks

Marks are used to style or add functionality to the text inside a `Text` node. 
For example, bold text, italic text, links, and custom styles like font or color.

### **Mark Types**

- **Bold**: Represents bold text.
- **Italic**: Represents italic text.
- **TextStyle**: Allows customization of font and color.
- **Link**: Represents a hyperlink.

Marks are validated and enforced with the help of `Pydantic` model validators.

## 🧩 Attributes

Attributes are optional fields that can store extra information for each node. Some predefined attributes include:

- `BoundingBox`: A box that specifies the position of a text in the page.
- `DocumentAttributes`: General attributes for the document.
- `PageAttributes`: Specific attributes like page number for the page.
- `TextAttributes`: Attributes such as bounding boxes for the text.

## 🏗️ Installation

The library `document-model-python` is distributed with PyPI, and you can easily install it with `pip`:

```bash
pip install document-model-python
```

## 🚀 Quick Example

Here’s how you can represent a simple document with one page and some text:

```python
from document_model_python.document import Document, Page, Text

doc = Document(
    category="doc",
    content=[
        Page(
            category="page",
            content=[
                Text(
                    category="heading",
                    content="Welcome to document-model-python",
                    marks=["bold"]
                ),
                Text(
                    category="body",
                    content="This is an example text using the document model."
                )
            ]
        )
    ]
)
```

## 💡 Contributing

Feel free to submit issues or contribute to the development of this library. We appreciate your feedback!

## 📜 License

This project is licensed under the MIT License.
