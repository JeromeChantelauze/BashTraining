#!/usr/bin/env python3
import sys
import os

class LinuxCmd:

    def list_items(self, args):
        cmd="ls"
        if len(args) > 0:
            for arg in args:
                cmd=cmd+" "+arg
        os.system(cmd)

    def move(self, file1, file2):
        Cmd="mv -v "+file1+" "+file2
        os.system(Cmd)

    def copy(self, args):
        cmd="cp -v "
        for arg in args:
            cmd=cmd+" "+arg
        os.system(cmd)

    def remove(self, args):
        cmd="rm -v "
        for arg in args:
            cmd=cmd+" "+arg
        os.system(cmd)

    def create(self, args):
        for arg in args:
            if os.path.exists(arg):
                continue
            cmd="touch "+arg
            if os.system(cmd)==0:
                print("Created '"+arg+"'")

    def create_dir(self, args):
        for arg in args:
            if os.path.exists(arg):
                continue
            cmd="mkdir "+arg
            if os.system(cmd)==0:
                print("Created '"+arg+"/'")



lc=LinuxCmd()

Cmd=sys.argv[1]

if Cmd=="list_items":
    lc.list_items(sys.argv[2:])
elif Cmd=="move":
    if len(sys.argv)!=4:
        print("Usage : move SRC DEST")
    else:
        lc.move(sys.argv[2], sys.argv[3])
elif Cmd=="copy":
    if len(sys.argv)<4:
        print("Usage : copy SRC [SRCs] DEST")
    else:
        lc.copy(sys.argv[2:])
elif Cmd=="remove":
    if len(sys.argv)<3:
        print("Usage : remove SRC [SRCs]")
    else:
        lc.remove(sys.argv[2:])
elif Cmd=="create":
    if len(sys.argv)<3:
        print("Usage : create SRC [SRCs]")
    else:
        lc.create(sys.argv[2:])
elif Cmd=="create_dir":
    if len(sys.argv)<3:
        print("Usage : create_dir SRC [SRCs]")
    else:
        lc.create_dir(sys.argv[2:])
else:
    print(Cmd+" : Unknown command")
        
