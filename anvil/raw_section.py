from typing import List, Tuple, Sequence, Iterable
from . import EmptySection, Block
from .errors import OutOfBoundsCoordinates
from .versions import VERSIONS
import array
from nbt import nbt

def bin_append(a, b, length=None):
    length = length or b.bit_length()
    return (a << length) | b

class RawSection(EmptySection):
    # TODO: fix
    """
    Same as :class:`EmptySection` but you manually
    set the palette, blocks array and the version (which instead
    of :class:`Block`, it's indexes on the palette)
    
    Attributes
    ----------
    y: :class:`int`
        Section's Y index
    blocks: Iterable[:class:`int`]
        Array of palette indexes
    _palette: Sequence[:class:`Block`]
        Section's palette
    version: VERSION
        data_version for the section to be generated
    """
    __slots__ = ('y', '_palette', 'blocks')
    def __init__(self, y: int, blocks: List[Block], palette: Sequence[Block]):
        super().__init__(y)
        self.blocks = blocks
        self._palette: Sequence[Block] = palette


    def palette(self) -> Sequence[Block]:
        """Returns ``self._palette``"""
        return self._palette
