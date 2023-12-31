"""
This type stub file was generated by pyright.
"""

from docx.parts.story import BaseStoryPart
from docx.shared import lazyproperty

"""|DocumentPart| and closely related objects"""
class DocumentPart(BaseStoryPart):
    """Main document part of a WordprocessingML (WML) package, aka a .docx file.

    Acts as broker to other parts such as image, core properties, and style parts. It
    also acts as a convenient delegate when a mid-document object needs a service
    involving a remote ancestor. The `Parented.part` property inherited by many content
    objects provides access to this part object for that purpose.
    """
    def add_footer_part(self): # -> tuple[FooterPart, Any]:
        """Return (footer_part, rId) pair for newly-created footer part."""
        ...
    
    def add_header_part(self): # -> tuple[HeaderPart, Any]:
        """Return (header_part, rId) pair for newly-created header part."""
        ...
    
    @property
    def core_properties(self):
        """
        A |CoreProperties| object providing read/write access to the core
        properties of this document.
        """
        ...
    
    @property
    def document(self): # -> Document:
        """
        A |Document| object providing access to the content of this document.
        """
        ...
    
    def drop_header_part(self, rId): # -> None:
        """Remove related header part identified by *rId*."""
        ...
    
    def footer_part(self, rId): # -> Any:
        """Return |FooterPart| related by *rId*."""
        ...
    
    def get_style(self, style_id, style_type): # -> Any | None:
        """
        Return the style in this document matching *style_id*. Returns the
        default style for *style_type* if *style_id* is |None| or does not
        match a defined style of *style_type*.
        """
        ...
    
    def get_style_id(self, style_or_name, style_type): # -> Any | None:
        """
        Return the style_id (|str|) of the style of *style_type* matching
        *style_or_name*. Returns |None| if the style resolves to the default
        style for *style_type* or if *style_or_name* is itself |None|. Raises
        if *style_or_name* is a style of the wrong type or names a style not
        present in the document.
        """
        ...
    
    def header_part(self, rId): # -> Any:
        """Return |HeaderPart| related by *rId*."""
        ...
    
    @lazyproperty
    def inline_shapes(self): # -> InlineShapes:
        """
        The |InlineShapes| instance containing the inline shapes in the
        document.
        """
        ...
    
    @lazyproperty
    def numbering_part(self): # -> Any:
        """
        A |NumberingPart| object providing access to the numbering
        definitions for this document. Creates an empty numbering part if one
        is not present.
        """
        ...
    
    def save(self, path_or_stream): # -> None:
        """
        Save this document to *path_or_stream*, which can be either a path to
        a filesystem location (a string) or a file-like object.
        """
        ...
    
    @property
    def settings(self): # -> Any | Settings:
        """
        A |Settings| object providing access to the settings in the settings
        part of this document.
        """
        ...
    
    @property
    def styles(self): # -> Any | Styles:
        """
        A |Styles| object providing access to the styles in the styles part
        of this document.
        """
        ...
    


