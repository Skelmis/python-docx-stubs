"""
This type stub file was generated by pyright.
"""

"""
Directly exposed API functions and classes, :func:`Document` for now.
Provides a syntactically more convenient API for interacting with the
OpcPackage graph.
"""
from document import Document as Doc

def Document(docx=...) -> Doc:
    """
    Return a |Document| object loaded from *docx*, where *docx* can be
    either a path to a ``.docx`` file (a string) or a file-like object. If
    *docx* is missing or ``None``, the built-in default document "template"
    is loaded.
    """
    ...

