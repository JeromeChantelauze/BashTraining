#!/usr/bin/env python3

def  Get_TS(Str):
    TS=""
    if len(Str)>18:
        TS=Str[6:18]
    return TS


def Get_Last_Word(Str):
    LW=""
    for idx in range(len(Str)-1, 18, -1):
        if Str[idx]!=" ":
            LW=Str[idx]+LW
        else:
            break
    return LW


LastWords=list()

FH=open("logcat_applications.txt", "r")
Str=FH.readline()
while Str!=None:
    TS=Get_TS(Str)
    if TS>"17:56:08.357":
        break
    elif TS>="17:56:07.996":
        LastWord=Get_Last_Word(Str)
        LastWords.append(LastWord)

    Str=FH.readline()

print(LastWords)

FH.close()
