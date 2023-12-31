"""
This type stub file was generated by pyright.
"""

from ..opc.part import XmlPart

"""
|SettingsPart| and closely related objects
"""
class SettingsPart(XmlPart):
    """
    Document-level settings part of a WordprocessingML (WML) package.
    """
    @classmethod
    def default(cls, package): # -> Self@SettingsPart:
        """
        Return a newly created settings part, containing a default
        `w:settings` element tree.
        """
        ...
    
    @property
    def settings(self): # -> Settings:
        """
        A |Settings| proxy object for the `w:settings` element in this part,
        containing the document-level settings for this document.
        """
        ...
    


