"""
This type stub file was generated by pyright.
"""

from docx.opc.shared import lazyproperty

"""Objects that implement reading and writing OPC packages."""
class OpcPackage:
    """Main API class for |python-opc|.

    A new instance is constructed by calling the :meth:`open` class method with a path
    to a package file or file-like object containing one.
    """
    def __init__(self) -> None:
        ...
    
    def after_unmarshal(self): # -> None:
        """
        Entry point for any post-unmarshaling processing. May be overridden
        by subclasses without forwarding call to super.
        """
        ...
    
    @property
    def core_properties(self): # -> Any | CoreProperties:
        """
        |CoreProperties| object providing read/write access to the Dublin
        Core properties for this document.
        """
        ...
    
    def iter_rels(self): # -> Generator[Any | Unknown, Any, None]:
        """
        Generate exactly one reference to each relationship in the package by
        performing a depth-first traversal of the rels graph.
        """
        ...
    
    def iter_parts(self): # -> Generator[Any | Unknown, Any, None]:
        """
        Generate exactly one reference to each of the parts in the package by
        performing a depth-first traversal of the rels graph.
        """
        ...
    
    def load_rel(self, reltype, target, rId, is_external=...): # -> Any:
        """
        Return newly added |_Relationship| instance of *reltype* between this
        part and *target* with key *rId*. Target mode is set to
        ``RTM.EXTERNAL`` if *is_external* is |True|. Intended for use during
        load from a serialized package, where the rId is well known. Other
        methods exist for adding a new relationship to the package during
        processing.
        """
        ...
    
    @property
    def main_document_part(self): # -> Any:
        """
        Return a reference to the main document part for this package.
        Examples include a document part for a WordprocessingML package, a
        presentation part for a PresentationML package, or a workbook part
        for a SpreadsheetML package.
        """
        ...
    
    def next_partname(self, template): # -> PackURI | None:
        """Return a |PackURI| instance representing partname matching *template*.

        The returned part-name has the next available numeric suffix to distinguish it
        from other parts of its type. *template* is a printf (%)-style template string
        containing a single replacement item, a '%d' to be used to insert the integer
        portion of the partname. Example: "/word/header%d.xml"
        """
        ...
    
    @classmethod
    def open(cls, pkg_file): # -> Self@OpcPackage:
        """
        Return an |OpcPackage| instance loaded with the contents of
        *pkg_file*.
        """
        ...
    
    def part_related_by(self, reltype): # -> Any:
        """
        Return part to which this package has a relationship of *reltype*.
        Raises |KeyError| if no such relationship is found and |ValueError|
        if more than one such relationship is found.
        """
        ...
    
    @property
    def parts(self): # -> list[Any | Unknown]:
        """
        Return a list containing a reference to each of the parts in this
        package.
        """
        ...
    
    def relate_to(self, part, reltype): # -> Any:
        """
        Return rId key of relationship to *part*, from the existing
        relationship if there is one, otherwise a newly created one.
        """
        ...
    
    @lazyproperty
    def rels(self): # -> Relationships:
        """
        Return a reference to the |Relationships| instance holding the
        collection of relationships for this package.
        """
        ...
    
    def save(self, pkg_file): # -> None:
        """
        Save this package to *pkg_file*, where *file* can be either a path to
        a file (a string) or a file-like object.
        """
        ...
    


class Unmarshaller:
    """Hosts static methods for unmarshalling a package from a |PackageReader|."""
    @staticmethod
    def unmarshal(pkg_reader, package, part_factory): # -> None:
        """
        Construct graph of parts and realized relationships based on the
        contents of *pkg_reader*, delegating construction of each part to
        *part_factory*. Package relationships are added to *pkg*.
        """
        ...
    

