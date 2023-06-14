"""
This type stub file was generated by pyright.
"""

from .base import XmlEnumeration, alias

"""
Enumerations related to styles
"""
@alias('WD_STYLE')
class WD_BUILTIN_STYLE(XmlEnumeration):
    """
    alias: **WD_STYLE**

    Specifies a built-in Microsoft Word style.

    Example::

        from docx import Document
        from docx.enum.style import WD_STYLE

        document = Document()
        styles = document.styles
        style = styles[WD_STYLE.BODY_TEXT]
    """
    __ms_name__ = ...
    __url__ = ...
    __members__ = ...

WD_STYLE = WD_BUILTIN_STYLE

class WD_STYLE_TYPE(XmlEnumeration):
    """
    Specifies one of the four style types: paragraph, character, list, or
    table.

    Example::

        from docx import Document
        from docx.enum.style import WD_STYLE_TYPE

        styles = Document().styles
        assert styles[0].type == WD_STYLE_TYPE.PARAGRAPH
    """
    __ms_name__ = ...
    __url__ = ...
    __members__ = ...


