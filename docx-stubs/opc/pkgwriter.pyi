"""
This type stub file was generated by pyright.
"""

"""
Provides a low-level, write-only API to a serialized Open Packaging
Convention (OPC) package, essentially an implementation of OpcPackage.save()
"""
class PackageWriter:
    """
    Writes a zip-format OPC package to *pkg_file*, where *pkg_file* can be
    either a path to a zip file (a string) or a file-like object. Its single
    API method, :meth:`write`, is static, so this class is not intended to
    be instantiated.
    """
    @staticmethod
    def write(pkg_file, pkg_rels, parts): # -> None:
        """
        Write a physical package (.pptx file) to *pkg_file* containing
        *pkg_rels* and *parts* and a content types stream based on the
        content types of the parts.
        """
        ...
    


class _ContentTypesItem:
    """
    Service class that composes a content types item ([Content_Types].xml)
    based on a list of parts. Not meant to be instantiated directly, its
    single interface method is xml_for(), e.g.
    ``_ContentTypesItem.xml_for(parts)``.
    """
    def __init__(self) -> None:
        ...
    
    @property
    def blob(self):
        """
        Return XML form of this content types item, suitable for storage as
        ``[Content_Types].xml`` in an OPC package.
        """
        ...
    
    @classmethod
    def from_parts(cls, parts): # -> Self@_ContentTypesItem:
        """
        Return content types XML mapping each part in *parts* to the
        appropriate content type and suitable for storage as
        ``[Content_Types].xml`` in an OPC package.
        """
        ...
    


