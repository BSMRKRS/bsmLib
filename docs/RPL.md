# RoboPiLib (RPL)

Library for RoboPi hat. We did not create RoboPiLib nor the hat. We have only
packaged it here, with minor changes to version v0.98 (v0.98 added `RPL.pwmWrite()` function).
[More info about RoboPi hat and Library](http://www.mikronauts.com/raspberry-pi/robopi/)

## RoboPi Reference

[RoboPi Reference](/docs/RoboPi_Reference.md) - BSMRKRS's instructions for operating Raspberry Pi w/ RoboPi hat </br>
[Offical RoboPi Documentation](http://www.mikronauts.com/raspberry-pi/robopi/) - Offical documentation by Mikronauts

## Constants

Pin Types: </br>
`INPUT` - Input pin mode </br>
`OUTPUT` - Output pin mode </br>
`PWM` - PWM pin mode </br>
`SERVO` - Servo pin mode </br>

Packet Identifiers: </br>
`GETINFO` - Returns product string </br>
`READMODE` - Read pin mode </br>
`WRITEMODE` - Write pin </br>
`DIGREAD` - Digital read </br>
`ANREAD` - Analog rad 10 bit result </br>
`ANREADRAW` - Analog read at raw resolution </br>
`ANWRITE` - Analog write 0 to 255 for PWM </br>
`SERVOWRITE` - Write a servo 0 to 20000us </br>
`SERVOREAD` - Read last value written to servo </br>
`READDIST` - Read distance sensor </br>
`PULSEGEN` - Start high frequency pulse train generator </br>
`PULSESTOP` - Stop pulse train generator </br>
`PWMWRITE` - Arbitrary PWM generator </br>

Miscellaneous: </br>
`API_REVISION` - API version </br>
`myaddr` - Default RoboPi address </br>
`ser` - Defualt RoboPi serial </br>

## Functions

`RPL.init(device = "/dev/ttyAMA0", bps = 115200)` - Init RoboPiLib </br>
`RPL.RoboPiInit(device = "/dev/ttyAMA0", bps = 115200)` - Same as `RPL.init()` but left for compatibility reasons </br>
`RPL.RoboPiExit()` - End serial connection w/ RoboPi hat </br>

`RPL.Address(n)` - Set address value </br>
`RPL.getProductID()` - Returns product RoboPi had product id </br>
`RPL.getAPIRev()` - Returns API version </br>

`RPL.pinMode(pin, mode)` - Set pin mode </br>
`RPL.readMode(pin)` - Returns pin mode </br>
`RPL.digitalWrite(pin, val)` - Sets pin to 0 or 1 </br>
`RPL.digitalRead(pin)` - Returns state of pin; 0 or 1 </br>
`RPL.analogRead(chan)` - Returns state of pin; 0 to 1023 </br>
`RPL.analogReadRaw(pin)` - Returns state of pin;  0 to 4095 </br>
`RPL.analogWrite(pin, val)` - Writes value (0 to 255) to PWM pin </br>
`RPL.servoWrite(pin, val)` - Sets servo pin to value (0 to 2500) </br>
`RPL.serovRead(pin)` - Returns last value written to servo pin </br>
`RPL.readDistance(pin)` - Returns distance to nearest object in millimeters </br>

`RPL.putPacket(cmd, buffr, plen)` - Send custom packet to RoboPi hat </br>
`RPL.getPacket()` - Returns packets send to RoboPi </br>
</br>
`RPL.pusleGen()` - Start high frequency pulse train generator </br>
`RPL.pulseStop()` - Stop pulse train generator </br>
`RPL.pwmWrite(pin, pulse, period)` - Sends pwm pulse to pin </br>

## Example

```python
from bsmLib import RPL

RPL.init()
RPL.servoWrite(0, 1000)
```
