"""
This type stub file was generated by pyright.
"""

from .image import BaseImageHeader

class Bmp(BaseImageHeader):
    """
    Image header parser for BMP images
    """
    @classmethod
    def from_stream(cls, stream): # -> Self@Bmp:
        """
        Return |Bmp| instance having header properties parsed from the BMP
        image in *stream*.
        """
        ...
    
    @property
    def content_type(self): # -> Literal['image/bmp']:
        """
        MIME content type for this image, unconditionally `image/bmp` for
        BMP images.
        """
        ...
    
    @property
    def default_ext(self): # -> Literal['bmp']:
        """
        Default filename extension, always 'bmp' for BMP images.
        """
        ...
    


