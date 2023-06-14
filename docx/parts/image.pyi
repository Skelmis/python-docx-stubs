"""
This type stub file was generated by pyright.
"""

from docx.opc.part import Part

"""
The proxy class for an image part, and related objects.
"""
class ImagePart(Part):
    """
    An image part. Corresponds to the target part of a relationship with type
    RELATIONSHIP_TYPE.IMAGE.
    """
    def __init__(self, partname, content_type, blob, image=...) -> None:
        ...
    
    @property
    def default_cx(self): # -> Inches:
        """
        Native width of this image, calculated from its width in pixels and
        horizontal dots per inch (dpi).
        """
        ...
    
    @property
    def default_cy(self): # -> Emu:
        """
        Native height of this image, calculated from its height in pixels and
        vertical dots per inch (dpi).
        """
        ...
    
    @property
    def filename(self): # -> str:
        """
        Filename from which this image part was originally created. A generic
        name, e.g. 'image.png', is substituted if no name is available, for
        example when the image was loaded from an unnamed stream. In that
        case a default extension is applied based on the detected MIME type
        of the image.
        """
        ...
    
    @classmethod
    def from_image(cls, image, partname): # -> ImagePart:
        """
        Return an |ImagePart| instance newly created from *image* and
        assigned *partname*.
        """
        ...
    
    @property
    def image(self): # -> Image:
        ...
    
    @classmethod
    def load(cls, partname, content_type, blob, package): # -> Self@ImagePart:
        """
        Called by ``docx.opc.package.PartFactory`` to load an image part from
        a package being opened by ``Document(...)`` call.
        """
        ...
    
    @property
    def sha1(self): # -> str:
        """
        SHA1 hash digest of the blob of this image part.
        """
        ...
    


