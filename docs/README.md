# Welcome to BSM Lib

Python Library Created For BSM Robotics. Tested on Python versions 2.7 & 3

## Install

```bash
git clone https://github.com/BSMRKRS/bsmLib/ && cd bsmLib
```

**Python 2.7:**

```bash
python setup.py install
```

**Python 3:**

```bash
python3 setup.py install
```

## Modules

[controller](/docs/controller.md) - Game controller class </br>
[hidePrints](/docs/hidePrints.md) - Hides print to console called by any function </br>
[networking](/docs/networking.md) - Networking classes </br>
[RPL](/docs/RPL.md) - RoboPiLib: Communicate w/ RoboPi hat </br>
[vector](/docs/vector.md) - Vector math class </br>

## RoboPi Reference

[RoboPi Reference](/docs/RoboPi_Reference.md) - BSMRKRS's instructions for operating Raspberry Pi w/ RoboPi hat </br>
[Offical RoboPi Documentation](http://www.mikronauts.com/raspberry-pi/robopi/) - Offical documentation by Mikronauts

## Misc Functions

`clear` - Clears Console </br>
`map(value, old_min, old_max, new_min, new_max)` - Returns value mapped to new range </br>

## Example

```python
from bsmLib import *

RPL.init() # Init RoboPi
RPL.servoWrite(0, 1000) # Write to pin 0
```

or

```python
import bsmLib

bsmLib.RPL.init() # Init RoboPi
bsmLib.RPL.servoWrite(0, 1000) # Write to pin 0
```

\*More examples can be found in the examples folder

## Dependencies

- serial - RoboPiLib
- PyGame - Controller

## Troubleshooting

#### Installation error:

Try to install w/ sudo

**Python 2.7**
```bash
sudo -H python setup.py install
```

**Python 3**
```bash
sudo -H python3 setup.py install
```

#### Run Error:

Reinstall Dependencies </br>

**Python 2.7**
```bash
pip install pygame
pip install serial
```

**Python 3**
```bash
pip3 install pygame
pip3 install serial
```

## License

[License](/docs/LICENSE)
