"""
This type stub file was generated by pyright.
"""

"""
Provides a low-level, read-only API to a serialized Open Packaging Convention
(OPC) package.
"""
class PackageReader:
    """
    Provides access to the contents of a zip-format OPC package via its
    :attr:`serialized_parts` and :attr:`pkg_srels` attributes.
    """
    def __init__(self, content_types, pkg_srels, sparts) -> None:
        ...
    
    @staticmethod
    def from_file(pkg_file): # -> PackageReader:
        """
        Return a |PackageReader| instance loaded with contents of *pkg_file*.
        """
        ...
    
    def iter_sparts(self): # -> Generator[tuple[Unknown, Unknown, Unknown, Unknown], Any, None]:
        """
        Generate a 4-tuple `(partname, content_type, reltype, blob)` for each
        of the serialized parts in the package.
        """
        ...
    
    def iter_srels(self): # -> Generator[tuple[PackURI, Unknown] | tuple[Unknown, Unknown], Any, None]:
        """
        Generate a 2-tuple `(source_uri, srel)` for each of the relationships
        in the package.
        """
        ...
    


class _ContentTypeMap:
    """
    Value type providing dictionary semantics for looking up content type by
    part name, e.g. ``content_type = cti['/ppt/presentation.xml']``.
    """
    def __init__(self) -> None:
        ...
    
    def __getitem__(self, partname):
        """
        Return content type for part identified by *partname*.
        """
        ...
    
    @staticmethod
    def from_xml(content_types_xml): # -> _ContentTypeMap:
        """
        Return a new |_ContentTypeMap| instance populated with the contents
        of *content_types_xml*.
        """
        ...
    


class _SerializedPart:
    """
    Value object for an OPC package part. Provides access to the partname,
    content type, blob, and serialized relationships for the part.
    """
    def __init__(self, partname, content_type, reltype, blob, srels) -> None:
        ...
    
    @property
    def partname(self): # -> Unknown:
        ...
    
    @property
    def content_type(self): # -> Unknown:
        ...
    
    @property
    def blob(self): # -> Unknown:
        ...
    
    @property
    def reltype(self): # -> Unknown:
        """
        The referring relationship type of this part.
        """
        ...
    
    @property
    def srels(self): # -> Unknown:
        ...
    


class _SerializedRelationship:
    """
    Value object representing a serialized relationship in an OPC package.
    Serialized, in this case, means any target part is referred to via its
    partname rather than a direct link to an in-memory |Part| object.
    """
    def __init__(self, baseURI, rel_elm) -> None:
        ...
    
    @property
    def is_external(self):
        """
        True if target_mode is ``RTM.EXTERNAL``
        """
        ...
    
    @property
    def reltype(self):
        """Relationship type, like ``RT.OFFICE_DOCUMENT``"""
        ...
    
    @property
    def rId(self):
        """
        Relationship id, like 'rId9', corresponds to the ``Id`` attribute on
        the ``CT_Relationship`` element.
        """
        ...
    
    @property
    def target_mode(self):
        """
        String in ``TargetMode`` attribute of ``CT_Relationship`` element,
        one of ``RTM.INTERNAL`` or ``RTM.EXTERNAL``.
        """
        ...
    
    @property
    def target_ref(self):
        """
        String in ``Target`` attribute of ``CT_Relationship`` element, a
        relative part reference for internal target mode or an arbitrary URI,
        e.g. an HTTP URL, for external target mode.
        """
        ...
    
    @property
    def target_partname(self): # -> PackURI:
        """
        |PackURI| instance containing partname targeted by this relationship.
        Raises ``ValueError`` on reference if target_mode is ``'External'``.
        Use :attr:`target_mode` to check before referencing.
        """
        ...
    


class _SerializedRelationships:
    """
    Read-only sequence of |_SerializedRelationship| instances corresponding
    to the relationships item XML passed to constructor.
    """
    def __init__(self) -> None:
        ...
    
    def __iter__(self): # -> Iterator[Unknown]:
        """Support iteration, e.g. 'for x in srels:'"""
        ...
    
    @staticmethod
    def load_from_xml(baseURI, rels_item_xml): # -> _SerializedRelationships:
        """
        Return |_SerializedRelationships| instance loaded with the
        relationships contained in *rels_item_xml*. Returns an empty
        collection if *rels_item_xml* is |None|.
        """
        ...
    

