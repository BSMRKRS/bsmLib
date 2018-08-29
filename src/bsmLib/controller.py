# bsmLib/controller.py
# Basic Class for Xbox Controller

# MIT License
#
# Copyright (c) 2018 BSMRKRS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from sys import platform
from bsmLib.hidePrints import hidePrints
with hidePrints():
    from pygame import event, joystick, display

win = platform.startswith("win")
darwin = platform.startswith("darwin")
lin = platform.startswith("lin")

if lin:
    # Buttons
    A = 0
    B = 1
    X = 2
    Y = 3
    LB = 4
    RB = 5
    SELECT = 6
    START = 7
    XBOX = 8
    LS = 9
    RS = 10

    # Axes
    LX = 0
    LY = 1
    LT = 2
    RT = 5
    RX = 3
    RY = 4

    # Dpad 0 for buttons 1 for hat
    PAD = 1

elif darwin:
    # Buttons
    A = 11
    B = 12
    X = 13
    Y = 14
    LB = 8
    RB = 9
    SELECT = 5
    START = 4
    XBOX = 10
    LS = 6
    RS = 7

    # Axes
    LX = 0
    LY = 1
    LT = 4
    RT = 5
    RX = 2
    RY = 3

    # Dpad 0 for buttons 1 for hat
    PAD = 0

elif win:
    # Buttons
    A = 0
    B = 1
    X = 2
    Y = 3
    LB = 4
    RB = 5
    SELECT = 6
    START = 7
    XBOX = None # Xbox button not supported on Windows offical driver
    LS = 8
    RS = 9

    # Axes
    LX = 0
    LY = 1
    LT = 2
    RT = 2
    RX = 3
    RY = 4

    # Dpad 0 for buttons 1 for hat
    PAD = 1

else:
    print("Error: Can't determine OS")
    exit()

class controller:
    '''
    Pygame Controller Class
    '''

    def __str__(c):
        '''
        Converts controller object to str
        '''
        a = (c.LX, c.LY, c.RX, c.RY, c.LT, c.RT)
        b = (c.A, c.B, c.X, c.Y, c.LB, c.RB, c.SELECT, c.START, c.XBOX, c.LS, \
        c.RS)
        d = (c.DX, c.DY)
        s = "Axis:\n%s\nButtons:\n%s\nDpad:\n%s" % (a, b, d)
        return s

    def __init__(self, id = 0, deadzone = .2):
        '''
        Creats controller object
        '''
        display.init()
        joystick.init()
        self.joystick = joystick.Joystick(id)
        self.joystick.init()
        self.deadzone = deadzone

        # Controller Pressed Values
        self.A = 0
        self.B = 0
        self.X = 0
        self.Y = 0
        self.LB = 0
        self.RB = 0
        self.SELECT = 0
        self.START = 0
        self.XBOX = 0
        self.LS = 0
        self.RS = 0
        self.LX = 0
        self.LY = 0
        self.LT = 0
        self.RT = 0
        self.RX = 0
        self.RY = 0
        self.DX = 0
        self.DY = 0

    def axes(self):
        '''
        Update axes values
        '''
        event.get()
        lx = self.joystick.get_axis(LX)
        ly = self.joystick.get_axis(LY)
        rx = self.joystick.get_axis(RX)
        ry = self.joystick.get_axis(RY)

        if(-self.deadzone < lx < self.deadzone):
            self.LX = 0
        else:
            self.LX = self.joystick.get_axis(LX)
        if(-self.deadzone < ly < self.deadzone):
            self.LY = 0
        else:
            self.LY = -self.joystick.get_axis(LY)

        if(-self.deadzone < rx < self.deadzone):
            self.RX = 0
        else:
            self.RX = self.joystick.get_axis(RX)
        if(-self.deadzone < ry < self.deadzone):
            self.RY = 0
        else:
            self.RY = -self.joystick.get_axis(RY)

        if(LT == RT):
            T = self.joystick.get_axis(LT)
            L = (T * 2) - 1
            R = ((T * 2) + 1) * -1
            self.LT = L
            self.RT = R
        else:
            self.LT = self.joystick.get_axis(LT)
            self.RT = self.joystick.get_axis(RT)

    def buttons(self):
        '''
        Update button values
        '''
        event.get()
        self.A = self.joystick.get_button(A)
        self.B = self.joystick.get_button(B)
        self.X = self.joystick.get_button(X)
        self.Y = self.joystick.get_button(Y)
        self.LB = self.joystick.get_button(LB)
        self.RB = self.joystick.get_button(RB)
        self.SELECT = self.joystick.get_button(SELECT)
        self.START = self.joystick.get_button(START)
        if(lin or darwin):
            # XBOX Button not supported on Windows offical driver
            self.XBOX = self.joystick.get_button(XBOX)
        self.LS = self.joystick.get_button(LS)
        self.RS = self.joystick.get_button(RS)

    def dpad(self):
        '''
        Update dpad values
        '''
        event.get()
        if(PAD):
            h = self.joystick.get_hat(0)
            self.DX = h[0]
            self.DY = h[1]
        else:
            x = self.joystick.get_button(0) - self.joystick.get_button(1)
            y = self.joystick.get_button(3) - self.joystick.get_button(2)
            self.DX = x
            self.DY = y

    def update(self):
        '''
        Update all input values
        '''
        self.axes()
        self.buttons()
        self.dpad()
