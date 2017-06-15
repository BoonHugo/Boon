#!/usr/bin/env python

from pyA20.gpio import gpio
from pyA20.gpio import port
class Led(gpio,port):
    def __init__(self):
        gpio.__init__(self)
        port.__init__(self)
        self.init()
        self.setcfg(port.PA13, 1)
        self.setcfg(port.PA14, 1)
        self.setcfg(port.PA2, 1)
        self.output(port.PA2, 0)
        self.output(port.PA14, 0)
        self.output(port.PA13, 0)
    def Rouge(self):
        self.output(port.PA14, 1)


if __name__ == '__name__':
    toto = Led()
    toto.Rouge()
