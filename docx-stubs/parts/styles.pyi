"""
This type stub file was generated by pyright.
"""

from ..opc.part import XmlPart

"""
Provides StylesPart and related objects
"""
class StylesPart(XmlPart):
    """
    Proxy for the styles.xml part containing style definitions for a document
    or glossary.
    """
    @classmethod
    def default(cls, package): # -> Self@StylesPart:
        """
        Return a newly created styles part, containing a default set of
        elements.
        """
        ...
    
    @property
    def styles(self): # -> Styles:
        """
        The |_Styles| instance containing the styles (<w:style> element
        proxies) for this styles part.
        """
        ...
    


