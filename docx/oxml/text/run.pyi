"""
This type stub file was generated by pyright.
"""

from ..xmlchemy import BaseOxmlElement

"""
Custom element classes related to text runs (CT_R).
"""
class CT_Br(BaseOxmlElement):
    """
    ``<w:br>`` element, indicating a line, page, or column break in a run.
    """
    type = ...
    clear = ...


class CT_R(BaseOxmlElement):
    """
    ``<w:r>`` element, containing the properties and text for a run.
    """
    rPr = ...
    t = ...
    br = ...
    cr = ...
    tab = ...
    drawing = ...
    def add_t(self, text):
        """
        Return a newly added ``<w:t>`` element containing *text*.
        """
        ...
    
    def add_drawing(self, inline_or_anchor):
        """
        Return a newly appended ``CT_Drawing`` (``<w:drawing>``) child
        element having *inline_or_anchor* as its child.
        """
        ...
    
    def clear_content(self): # -> None:
        """
        Remove all child elements except the ``<w:rPr>`` element if present.
        """
        ...
    
    @property
    def style(self): # -> None:
        """
        String contained in w:val attribute of <w:rStyle> grandchild, or
        |None| if that element is not present.
        """
        ...
    
    @style.setter
    def style(self, style): # -> None:
        """
        Set the character style of this <w:r> element to *style*. If *style*
        is None, remove the style element.
        """
        ...
    
    @property
    def text(self): # -> LiteralString | Literal['']:
        """
        A string representing the textual content of this run, with content
        child elements like ``<w:tab/>`` translated to their Python
        equivalent.
        """
        ...
    
    @text.setter
    def text(self, text): # -> None:
        ...
    


class CT_Text(BaseOxmlElement):
    """
    ``<w:t>`` element, containing a sequence of characters within a run.
    """
    ...


class _RunContentAppender:
    """
    Service object that knows how to translate a Python string into run
    content elements appended to a specified ``<w:r>`` element. Contiguous
    sequences of regular characters are appended in a single ``<w:t>``
    element. Each tab character ('\t') causes a ``<w:tab/>`` element to be
    appended. Likewise a newline or carriage return character ('\n', '\r')
    causes a ``<w:cr>`` element to be appended.
    """
    def __init__(self, r) -> None:
        ...
    
    @classmethod
    def append_to_run_from_text(cls, r, text): # -> None:
        """
        Create a "one-shot" ``_RunContentAppender`` instance and use it to
        append the run content elements corresponding to *text* to the
        ``<w:r>`` element *r*.
        """
        ...
    
    def add_text(self, text): # -> None:
        """
        Append the run content elements corresponding to *text* to the
        ``<w:r>`` element of this instance.
        """
        ...
    
    def add_char(self, char): # -> None:
        """
        Process the next character of input through the translation finite
        state maching (FSM). There are two possible states, buffer pending
        and not pending, but those are hidden behind the ``.flush()`` method
        which must be called at the end of text to ensure any pending
        ``<w:t>`` element is written.
        """
        ...
    
    def flush(self): # -> None:
        ...
    


