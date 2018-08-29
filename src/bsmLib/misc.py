# bsmLib/misc.py
# Miscellaneous Python Functions

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
from os import system

win = platform.startswith("win")
darwin = platform.startswith("darwin")
lin = platform.startswith("lin")

def clear():
    '''
    Clears Console
    '''
    if win:
        system("CLS")
    else:
        system("clear")

def map(value, old_min, old_max, new_min, new_max):
    '''
    Returns value mapped to new range
    '''
    s0 = old_max - old_min
    s1 = new_max - new_min
    s = s1 / s0
    new_value = (value * s) + new_min + (s1 / 2)
    return new_value
