"""
This type stub file was generated by pyright.
"""

from ..xmlchemy import BaseOxmlElement

"""
Custom element classes related to paragraphs (CT_P).
"""
class CT_P(BaseOxmlElement):
    """
    ``<w:p>`` element, containing the properties and text for a paragraph.
    """
    pPr = ...
    r = ...
    def add_p_before(self):
        """
        Return a new ``<w:p>`` element inserted directly prior to this one.
        """
        ...
    
    @property
    def alignment(self): # -> None:
        """
        The value of the ``<w:jc>`` grandchild element or |None| if not
        present.
        """
        ...
    
    @alignment.setter
    def alignment(self, value): # -> None:
        ...
    
    def clear_content(self): # -> None:
        """
        Remove all child elements, except the ``<w:pPr>`` element if present.
        """
        ...
    
    def set_sectPr(self, sectPr): # -> None:
        """
        Unconditionally replace or add *sectPr* as a grandchild in the
        correct sequence.
        """
        ...
    
    @property
    def style(self): # -> None:
        """
        String contained in w:val attribute of ./w:pPr/w:pStyle grandchild,
        or |None| if not present.
        """
        ...
    
    @style.setter
    def style(self, style): # -> None:
        ...
    


