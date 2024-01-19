#!/usr/bin/env python3
import sys

def autonomy(level) :
    result=62*float(level)/15.6
    return result

Autonomy=autonomy(sys.argv[1])
print("Autonmy estimation : "+str(int(Autonomy))+" kilometers")
