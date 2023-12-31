"""
This type stub file was generated by pyright.
"""

from ..part import XmlPart

"""
Core properties part, corresponds to ``/docProps/core.xml`` part in package.
"""
class CorePropertiesPart(XmlPart):
    """
    Corresponds to part named ``/docProps/core.xml``, containing the core
    document properties for this document package.
    """
    @classmethod
    def default(cls, package): # -> CorePropertiesPart:
        """
        Return a new |CorePropertiesPart| object initialized with default
        values for its base properties.
        """
        ...
    
    @property
    def core_properties(self): # -> CoreProperties:
        """
        A |CoreProperties| object providing read/write access to the core
        properties contained in this core properties part.
        """
        ...
    


