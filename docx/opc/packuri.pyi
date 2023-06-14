"""
This type stub file was generated by pyright.
"""

"""
Provides the PackURI value type along with some useful known pack URI strings
such as PACKAGE_URI.
"""
class PackURI(str):
    """
    Provides access to pack URI components such as the baseURI and the
    filename slice. Behaves as |str| otherwise.
    """
    _filename_re = ...
    def __new__(cls, pack_uri_str): # -> Self@PackURI:
        ...
    
    @staticmethod
    def from_rel_ref(baseURI, relative_ref): # -> PackURI:
        """
        Return a |PackURI| instance containing the absolute pack URI formed by
        translating *relative_ref* onto *baseURI*.
        """
        ...
    
    @property
    def baseURI(self): # -> Self@PackURI:
        """
        The base URI of this pack URI, the directory portion, roughly
        speaking. E.g. ``'/ppt/slides'`` for ``'/ppt/slides/slide1.xml'``.
        For the package pseudo-partname '/', baseURI is '/'.
        """
        ...
    
    @property
    def ext(self): # -> str | Self@PackURI:
        """
        The extension portion of this pack URI, e.g. ``'xml'`` for
        ``'/word/document.xml'``. Note the period is not included.
        """
        ...
    
    @property
    def filename(self): # -> Self@PackURI:
        """
        The "filename" portion of this pack URI, e.g. ``'slide1.xml'`` for
        ``'/ppt/slides/slide1.xml'``. For the package pseudo-partname '/',
        filename is ''.
        """
        ...
    
    @property
    def idx(self): # -> int | None:
        """
        Return partname index as integer for tuple partname or None for
        singleton partname, e.g. ``21`` for ``'/ppt/slides/slide21.xml'`` and
        |None| for ``'/ppt/presentation.xml'``.
        """
        ...
    
    @property
    def membername(self): # -> str:
        """
        The pack URI with the leading slash stripped off, the form used as
        the Zip file membername for the package item. Returns '' for the
        package pseudo-partname '/'.
        """
        ...
    
    def relative_ref(self, baseURI): # -> str:
        """
        Return string containing relative reference to package item from
        *baseURI*. E.g. PackURI('/ppt/slideLayouts/slideLayout1.xml') would
        return '../slideLayouts/slideLayout1.xml' for baseURI '/ppt/slides'.
        """
        ...
    
    @property
    def rels_uri(self): # -> PackURI:
        """
        The pack URI of the .rels part corresponding to the current pack URI.
        Only produces sensible output if the pack URI is a partname or the
        package pseudo-partname '/'.
        """
        ...
    


PACKAGE_URI = ...
CONTENT_TYPES_URI = ...
