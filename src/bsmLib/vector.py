# bsmLib/vector.py
# Basic 2d Vector math

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


from math import sqrt, atan2, sin, cos

class vector:
    '''
    Basic Vector Math
    '''

    def __add__(v0, v1):
        '''
        Adds two vectors
        '''
        v = vector(v0.x + v1.x, v0.y + v1.y)
        return v

    def __sub__(v0, v1):
        '''
        Subtracts two vectors
        '''
        v = vector(v0.x - v1.x, v0.y - v1.y)
        return v

    def __mul__(v, s):
        '''
        Multiply vector by scalar
        '''
        v = vector(v.x * s, v.y * s)
        return v

    def __div__(v, s):
        '''
        Divides by scalar
        '''
        v = vector(v.x / s, v.y / s)
        return v

    def __str__(v):
        '''
        Returns x, y coordinates of vectors
        '''
        x = v.x
        y = v.y
        s = "(%d, %d)" % (x, y)
        return s

    def __init__(self, x = 0, y = 0):
        '''
        Create vector w/ (x, y) coordinates
        '''
        self.x = x
        self.y = y

    def copy(self):
        '''
        Returns copy of vector
        '''
        c = vector(self.x, self.y)
        return c

    def heading(self):
        '''
        Returns calculated heading
        '''
        x = self.x
        y = self.y
        a = atan2(y, x)
        return a

    def mag(self):
        '''
        Returns calculated magnitude
        '''
        x = self.x
        y = self.y
        mag = sqrt(x ** 2 + y ** 2)
        return mag

    def set(self, x, y):
        '''
        Sets new (x, y) coordinates for vectors
        '''
        self.x = x
        self.y = y

    def setHeading(self, heading):
        '''
        Set heading in radians
        '''
        m = self.mag()
        self.x = cos(heading) * m
        self.y = sin(heading) * m

    def setMag(self, m):
        '''
        Set magnitude
        '''
        s = m / self.mag()
        self.x *= s
        self.y *= s
