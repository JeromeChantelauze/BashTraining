#!/usr/bin/env python3
import numpy

ADAS_Frames=[
        [ 0x00, 0x06, 0x02, 0x08, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x05, 0xD0, 0x08, 0xFF, 0x60, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x06, 0x01, 0x08, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0xC7, 0x77, 0x8A, 0x70, 0xAB, 0xAF, 0x88, 0x2A, 0x8C ],
        [ 0x00, 0x06, 0x02, 0x08, 0x40, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x05, 0xD0, 0x08, 0x21, 0x20, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x06, 0x01, 0x08, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x11, 0x29, 0xFB, 0x84, 0x33, 0x1D, 0xE5, 0x5E, 0x9D ]
]

class byte:
    def __init__(self, val):
        self.value=val & 255

    def get(self, start, size):
        if size==0 or size>8:
            return None

        mask=0
        for idx in range(0, size):
            mask=128+(mask >> 1)

        mask=mask >> (7 - start)
        result=self.value & mask
        
        return result >> (start + 1 - size)

    def set(self, start, size, value):
        if size==0 or size>8:
            return

        mask=0
        for idx in range(0, size):
            mask=1+(mask << 1)
            
        rst=mask << (start + 1 - size)
        rst=(rst^255) & 255
        self.value=self.value & rst

        mask = mask & value
        mask=mask << (start + 1 - size)
        self.value=self.value | mask
        
def print_Frame(Array):
    Frame=numpy.array(Array)
    vhex = numpy.vectorize(hex)
    print(vhex(Frame))


for ADAS in ADAS_Frames:
    print_Frame(ADAS)
    Payload_idx=4
    B=byte(ADAS[Payload_idx+2])
    B.set(5, 2, 2)
    ADAS[Payload_idx+2]=B.value
    Payload_idx=17
    B=byte(ADAS[Payload_idx+4])
    B.set(7, 6, 45)
    ADAS[Payload_idx+2]=B.value
    Payload_idx=28
    B=byte(ADAS[Payload_idx+5])
    B.set(2, 1, 1)
    ADAS[Payload_idx+2]=B.value
    print_Frame(ADAS)
    print("======")
