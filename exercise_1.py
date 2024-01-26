#!/usr/bin/env python3

IVI_Frames=[
        [ 0x60, 0x20, 0x45, 0x6C, 0xFE, 0x3D, 0x4B, 0xAA ],
        [ 0x40, 0x12, 0x6C, 0xAF, 0x05, 0x78, 0x4A, 0x04 ]
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

for IVI_F in IVI_Frames:
    B=byte(IVI_F[0])
    PassengerSeatMemoRequest=B.get(7, 3)
    B=byte(IVI_F[5])
    ClimFPrightBlowingRequest=B.get(7, 4)
    TimeFormatDisplay=B.get(3, 1)
    print("PassengerSeatMemoRequest="+str(PassengerSeatMemoRequest))
    print("ClimFPrightBlowingRequest="+str(ClimFPrightBlowingRequest))
    print("TimeFormatDisplay="+str(TimeFormatDisplay))
    print("======")

