"""
This type stub file was generated by pyright.
"""

"""
Constants specific the the image sub-package
"""
class JPEG_MARKER_CODE:
    """
    JPEG marker codes
    """
    TEM = ...
    DHT = ...
    DAC = ...
    JPG = ...
    SOF0 = ...
    SOF1 = ...
    SOF2 = ...
    SOF3 = ...
    SOF5 = ...
    SOF6 = ...
    SOF7 = ...
    SOF9 = ...
    SOFA = ...
    SOFB = ...
    SOFD = ...
    SOFE = ...
    SOFF = ...
    RST0 = ...
    RST1 = ...
    RST2 = ...
    RST3 = ...
    RST4 = ...
    RST5 = ...
    RST6 = ...
    RST7 = ...
    SOI = ...
    EOI = ...
    SOS = ...
    DQT = ...
    DNL = ...
    DRI = ...
    DHP = ...
    EXP = ...
    APP0 = ...
    APP1 = ...
    APP2 = ...
    APP3 = ...
    APP4 = ...
    APP5 = ...
    APP6 = ...
    APP7 = ...
    APP8 = ...
    APP9 = ...
    APPA = ...
    APPB = ...
    APPC = ...
    APPD = ...
    APPE = ...
    APPF = ...
    STANDALONE_MARKERS = ...
    SOF_MARKER_CODES = ...
    marker_names = ...
    @classmethod
    def is_standalone(cls, marker_code): # -> bool:
        ...
    


class MIME_TYPE:
    """
    Image content types
    """
    BMP = ...
    GIF = ...
    JPEG = ...
    PNG = ...
    TIFF = ...


class PNG_CHUNK_TYPE:
    """
    PNG chunk type names
    """
    IHDR = ...
    pHYs = ...
    IEND = ...


class TIFF_FLD_TYPE:
    """
    Tag codes for TIFF Image File Directory (IFD) entries.
    """
    BYTE = ...
    ASCII = ...
    SHORT = ...
    LONG = ...
    RATIONAL = ...
    field_type_names = ...


TIFF_FLD = TIFF_FLD_TYPE
class TIFF_TAG:
    """
    Tag codes for TIFF Image File Directory (IFD) entries.
    """
    IMAGE_WIDTH = ...
    IMAGE_LENGTH = ...
    X_RESOLUTION = ...
    Y_RESOLUTION = ...
    RESOLUTION_UNIT = ...
    tag_names = ...

