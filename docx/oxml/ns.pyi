"""
This type stub file was generated by pyright.
"""

"""
Namespace-related objects.
"""
nsmap = ...
pfxmap = ...
class NamespacePrefixedTag(str):
    """
    Value object that knows the semantics of an XML tag having a namespace
    prefix.
    """
    def __new__(cls, nstag, *args): # -> Self@NamespacePrefixedTag:
        ...
    
    def __init__(self, nstag) -> None:
        ...
    
    @property
    def clark_name(self): # -> str:
        ...
    
    @classmethod
    def from_clark_name(cls, clark_name): # -> Self@NamespacePrefixedTag:
        ...
    
    @property
    def local_part(self):
        """
        Return the local part of the tag as a string. E.g. 'foobar' is
        returned for tag 'f:foobar'.
        """
        ...
    
    @property
    def nsmap(self): # -> dict[Unknown, str]:
        """
        Return a dict having a single member, mapping the namespace prefix of
        this tag to it's namespace name (e.g. {'f': 'http://foo/bar'}). This
        is handy for passing to xpath calls and other uses.
        """
        ...
    
    @property
    def nspfx(self):
        """
        Return the string namespace prefix for the tag, e.g. 'f' is returned
        for tag 'f:foobar'.
        """
        ...
    
    @property
    def nsuri(self): # -> str:
        """
        Return the namespace URI for the tag, e.g. 'http://foo/bar' would be
        returned for tag 'f:foobar' if the 'f' prefix maps to
        'http://foo/bar' in nsmap.
        """
        ...
    


def nsdecls(*prefixes): # -> str:
    """
    Return a string containing a namespace declaration for each of the
    namespace prefix strings, e.g. 'p', 'ct', passed as *prefixes*.
    """
    ...

def nspfxmap(*nspfxs): # -> dict[Unknown, str]:
    """
    Return a dict containing the subset namespace prefix mappings specified by
    *nspfxs*. Any number of namespace prefixes can be supplied, e.g.
    namespaces('a', 'r', 'p').
    """
    ...

def qn(tag): # -> str:
    """
    Stands for "qualified name", a utility function to turn a namespace
    prefixed tag name into a Clark-notation qualified tag name for lxml. For
    example, ``qn('p:cSld')`` returns ``'{http://schemas.../main}cSld'``.
    """
    ...

