# anvil-parser2
[![Documentation Status](https://readthedocs.org/projects/anvil-parser/badge/?version=latest)](https://anvil-parser.readthedocs.io/en/latest/?badge=latest)
[![Tests](https://github.com/0xTiger/anvil-parser/actions/workflows/run-pytest.yml/badge.svg)](https://github.com/0xTiger/anvil-parser/actions/workflows/run-pytest.yml)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/anvil-parser)](https://pypi.org/project/anvil-parser2/)

A parser for the [Minecraft anvil file format](https://minecraft.wiki/w/Anvil_file_format). This package was forked from [matcool's anvil-parser](https://github.com/matcool/anvil-parser) in order to additionally support minecraft versions 1.18 and above.
# Installation
```
pip install anvil-parser2
```

# Usage
## Reading
```python
import anvil

region = anvil.Region.from_file('r.0.0.mca')

# You can also provide the region file name instead of the object
chunk = anvil.Chunk.from_region(region, 0, 0)

# If `section` is not provided, will get it from the y coords
# and assume it's global
block = chunk.get_block(0, 0, 0)

print(block) # <Block(minecraft:air)>
print(block.id) # air
print(block.properties) # {}
```
## Making own regions
```python
import anvil
from random import choice

# Create a new region with the `EmptyRegion` class at 0, 0 (in region coords)
region = anvil.EmptyRegion(0, 0)

# Create `Block` objects that are used to set blocks
stone = anvil.Block('minecraft', 'stone')
dirt = anvil.Block('minecraft', 'dirt')

# Make a 16x16x16 cube of either stone or dirt blocks
for y in range(16):
    for z in range(16):
        for x in range(16):
            region.set_block(choice((stone, dirt)), x, y, z)

# Save to a file
region.save('r.0.0.mca')
```
### Version support
If you want to create regions for older versions, you need to set the version before you create your first region/chunk

Supported versions are found [here](anvil/versions.py). This only contains major Minecraft updates. If you want to see all versions, see [versions](https://minecraft.wiki/w/Data_version)

If you open an anvil file in a newer Minecraft version, it will automaticly convert it to the newer version, nevertheless it's not recomended.

```python
import anvil

# set the version, for example to 19w36a
anvil.config["version"] = anvil.VERSIONS.VERSION_19W36A

# region will be created for this specific version
region = anvil.EmptyRegion(0, 0)
region.save('r.0.0.mca')

```
> [!WARNING]
Don't change the version after the first creation of a region / section / chunk or the result will be corrupted

# Todo
*things to do before 1.0.0*
- [x] Proper documentation
- [x] Biomes
- [x] CI
- [ ] More tests
  - [ ] Tests for 20w17a+ BlockStates format
# Note
Testing done in 1.14.4 - 1.21, should work fine for other versions.
