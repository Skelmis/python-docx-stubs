"""
This type stub file was generated by pyright.
"""

from ..shared import ElementProxy

"""
Latent style-related objects.
"""
class LatentStyles(ElementProxy):
    """
    Provides access to the default behaviors for latent styles in this
    document and to the collection of |_LatentStyle| objects that define
    overrides of those defaults for a particular named latent style.
    """
    __slots__ = ...
    def __getitem__(self, key): # -> _LatentStyle:
        """
        Enables dictionary-style access to a latent style by name.
        """
        ...
    
    def __iter__(self): # -> Generator[_LatentStyle, None, None]:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def add_latent_style(self, name): # -> _LatentStyle:
        """
        Return a newly added |_LatentStyle| object to override the inherited
        defaults defined in this latent styles object for the built-in style
        having *name*.
        """
        ...
    
    @property
    def default_priority(self):
        """
        Integer between 0 and 99 inclusive specifying the default sort order
        for latent styles in style lists and the style gallery. |None| if no
        value is assigned, which causes Word to use the default value 99.
        """
        ...
    
    @default_priority.setter
    def default_priority(self, value): # -> None:
        ...
    
    @property
    def default_to_hidden(self):
        """
        Boolean specifying whether the default behavior for latent styles is
        to be hidden. A hidden style does not appear in the recommended list
        or in the style gallery.
        """
        ...
    
    @default_to_hidden.setter
    def default_to_hidden(self, value): # -> None:
        ...
    
    @property
    def default_to_locked(self):
        """
        Boolean specifying whether the default behavior for latent styles is
        to be locked. A locked style does not appear in the styles panel or
        the style gallery and cannot be applied to document content. This
        behavior is only active when formatting protection is turned on for
        the document (via the Developer menu).
        """
        ...
    
    @default_to_locked.setter
    def default_to_locked(self, value): # -> None:
        ...
    
    @property
    def default_to_quick_style(self):
        """
        Boolean specifying whether the default behavior for latent styles is
        to appear in the style gallery when not hidden.
        """
        ...
    
    @default_to_quick_style.setter
    def default_to_quick_style(self, value): # -> None:
        ...
    
    @property
    def default_to_unhide_when_used(self):
        """
        Boolean specifying whether the default behavior for latent styles is
        to be unhidden when first applied to content.
        """
        ...
    
    @default_to_unhide_when_used.setter
    def default_to_unhide_when_used(self, value): # -> None:
        ...
    
    @property
    def load_count(self):
        """
        Integer specifying the number of built-in styles to initialize to the
        defaults specified in this |LatentStyles| object. |None| if there is
        no setting in the XML (very uncommon). The default Word 2011 template
        sets this value to 276, accounting for the built-in styles in Word
        2010.
        """
        ...
    
    @load_count.setter
    def load_count(self, value): # -> None:
        ...
    


class _LatentStyle(ElementProxy):
    """
    Proxy for an `w:lsdException` element, which specifies display behaviors
    for a built-in style when no definition for that style is stored yet in
    the `styles.xml` part. The values in this element override the defaults
    specified in the parent `w:latentStyles` element.
    """
    __slots__ = ...
    def delete(self): # -> None:
        """
        Remove this latent style definition such that the defaults defined in
        the containing |LatentStyles| object provide the effective value for
        each of its attributes. Attempting to access any attributes on this
        object after calling this method will raise |AttributeError|.
        """
        ...
    
    @property
    def hidden(self):
        """
        Tri-state value specifying whether this latent style should appear in
        the recommended list. |None| indicates the effective value is
        inherited from the parent ``<w:latentStyles>`` element.
        """
        ...
    
    @hidden.setter
    def hidden(self, value): # -> None:
        ...
    
    @property
    def locked(self):
        """
        Tri-state value specifying whether this latent styles is locked.
        A locked style does not appear in the styles panel or the style
        gallery and cannot be applied to document content. This behavior is
        only active when formatting protection is turned on for the document
        (via the Developer menu).
        """
        ...
    
    @locked.setter
    def locked(self, value): # -> None:
        ...
    
    @property
    def name(self): # -> Literal['Caption', 'Footer', 'Header', 'Heading 1', 'Heading 2', 'Heading 3', 'Heading 4', 'Heading 5', 'Heading 6', 'Heading 7', 'Heading 8', 'Heading 9']:
        """
        The name of the built-in style this exception applies to.
        """
        ...
    
    @property
    def priority(self):
        """
        The integer sort key for this latent style in the Word UI.
        """
        ...
    
    @priority.setter
    def priority(self, value): # -> None:
        ...
    
    @property
    def quick_style(self):
        """
        Tri-state value specifying whether this latent style should appear in
        the Word styles gallery when not hidden. |None| indicates the
        effective value should be inherited from the default values in its
        parent |LatentStyles| object.
        """
        ...
    
    @quick_style.setter
    def quick_style(self, value): # -> None:
        ...
    
    @property
    def unhide_when_used(self):
        """
        Tri-state value specifying whether this style should have its
        :attr:`hidden` attribute set |False| the next time the style is
        applied to content. |None| indicates the effective value should be
        inherited from the default specified by its parent |LatentStyles|
        object.
        """
        ...
    
    @unhide_when_used.setter
    def unhide_when_used(self, value): # -> None:
        ...
    


