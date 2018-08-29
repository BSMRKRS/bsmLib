# Controller

Controller class written with pygame. Only tested with xbox controllers.

## Driver Install

Windows:
- Driver comes pre-installed

Mac:
- requires this driver https://github.com/360Controller/360Controller/releases
- If you are on High Sierra you will need to use this work arround to enable this driver's kext to load
  - Open "System Preferences" and click "Keyboard" then "Input Sources" and enable keyboard access to "All controls" </br>
  ![alt text](https://github.com/BSMRKRS/bsmLib/blob/master/docs/pics/keyboard.png)
  - In "System Preferences" go to "Security & Privacy" and hit tab until the allow button is highlighted and hit space or enter. </br>
  ![alt text](https://github.com/BSMRKRS/bsmLib/blob/master/docs/pics/allow.png)
  - This issue happens on High Sierra due to not allowing any kext to be allowed while a monitoring software/screen controlling software is running like "LanSchool"

Linux:
```bash
sudo git clone https://github.com/paroj/xpad.git /usr/src/xpad-0.4
sudo dkms install -m xpad -v 0.4
```

https://github.com/paroj/xpad

## Object Variables
`controller.A` - Digital value 0 or 1 for button "A" when pressed </br>
`controller.B` - Digital value 0 or 1 for button "B" when pressed </br>
`controller.X` - Digital value 0 or 1 for button "X" when pressed </br>
`controller.Y` - Digital value 0 or 1 for button "Y" when pressed </br>
`controller.LB` - Digital value 0 or 1 for button "LB" when pressed </br>
`controller.RB` - Digital value 0 or 1 for button "RB" when pressed </br>
`controller.SELECT` - Digital value 0 or 1 for button "SELECT" when pressed </br>
`controller.START` - Digital value 0 or 1 for button "START" when pressed </br>
`controller.XBOX` - Digital value 0 or 1 for button "XBOX" when pressed (Doesn't work on windows)</br>
`controller.LS` - Digital value 0 or 1 for button "LS" when pressed </br>
`controller.RS` - Digital value 0 or 1 for button "RS" when pressed </br>
</br>
`controller.LX` _ Analog value -1 to 1 for axis "LX" when pressed </br>
`controller.LY` _ Analog value -1 to 1 for axis "LY" when pressed </br>
`controller.RX` _ Analog value -1 to 1 for axis "RX" when pressed </br>
`controller.RY` _ Analog value -1 to 1 for axis "RY" when pressed </br>
`controller.LT` _ Analog value -1 to 1 for axis "LT" when pressed </br>
`controller.RT` _ Analog value -1 to 1 for axis "RT" when pressed </br>
</br>
`controller.DX` - Value of -1, 1, or 0 base on "DX" input of down, up, or none </br>
`controller.DY`- Value of -1, 1, or 0 base on "DX" input of left, right, or none </br>

## Functions
`controller.controller(id = 0, deadzone = .2)` - Create controller </br>
</br>
`controller.axes()` - Update axes values </br>
`controller.buttons()` - Update button values </br>
`controller.dpad()` - Update dpad values </br>
`controller.update()` - Update all input values </br>

## Example

```python
from bsmLib.controller import controller

c = controller()

while(1):
    c.update()
    print(c)
```
