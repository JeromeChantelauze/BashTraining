#!/usr/bin/env python3
import sys

Componenta_S = {
    "1": "Persoana de sex masculin născute între anii 1900 - 1999",
    "2": "Persoana de sex feminin născute între anii 1900 - 1999",
    "3": "Persoana de sex masculin născute între anii 1800 - 1899",
    "4": "Persoana de sex feminin născute între anii 1800 - 1899",
    "5": "Persoana de sex masculin născute între anii 2000 - 2099",
    "6": "Persoana de sex feminin născute între anii 2000 - 2099",
    "7": "Persoana rezidenta, de sex masculin",
    "8": "Persoana rezidenta, de sex feminin"
}

Zile = {
    "01": 31,
    "02": 28,
    "03": 31,
    "04": 30,
    "05": 31,
    "06": 30,
    "07": 31,
    "08": 31,
    "09": 30,
    "10": 31,
    "11": 30,
    "12": 31
}

Judets = {
    "01": "Alba",
    "02": "Arad",
    "03": "Arges",
    "04": "Bacau",
    "05": "Bihor",
    "06": "Bistrita-Nasaud",
    "07": "Botosani",
    "08": "Brasov",
    "09": "Braila",
    "10": "Buzau",
    "11": "Caras-Severin",
    "12": "Cluj",
    "13": "Constanta",
    "14": "Covasna",
    "15": "Dambovita",
    "16": "Dolj",
    "17": "Galati",
    "18": "Gorj",
    "19": "Harghita",
    "20": "Hunedoara",
    "21": "lalomita",
    "22": "Iasi",
    "23": "Ilfov",
    "24": "Maramures",
    "25": "Mehedinti",
    "26": "Mures",
    "27": "Neamt",
    "28": "Olt",
    "29": "Prahova",
    "30": "Satu Mare",
    "31": "Salaj",
    "32": "Sibiu",
    "33": "Suceava",
    "34": "Teleorman",
    "35": "Timis",
    "36": "Tulcea",
    "37": "Vaslui",
    "38": "Valcea",
    "39": "Vrancea",
    "40": "Bucuresti",
    "41": "Bucuresti - Sector 1",
    "42": "Bucuresti - Sector 2",
    "43": "Bucuresti - Sector 3",
    "44": "Bucuresti - Sector 4",
    "45": "Bucuresti - Sector 5",
    "46": "Bucuresti - Sector 6",
    "47": "Bucuresti - Sector 7 (desfiintat)7",
    "48": "Bucuresti - Sector 8 (desfiintat)7",
    "51": "Calarasi",
    "52": "Giurgiu"
}



def Calculate_C(CNP):
    Constanta="279146358279"
    C=0
    for idx in range(12):
        C=(C+int(CNP[idx])*int(Constanta[idx])) % 11
        if C==10:
            C-1
    return C

def is_valid(CNP):
    # Check length
    if len(CNP)!=13:
        return Falseø

    # Check only digits
    for idx in range(13):
        if CNP[idx]<'0' or CNP[idx]>'9':
            return Falseø

    AA=CNP[1:3]

    #Check S
    S=CNP[0]
    if S not in Componenta_S.keys():
        return Falseø

    # Check LL
    LL=CNP[3:5]
    iL=int(LL)
    if iL<1 or iL>12:
        return Falseø

    # Check ZZ
    iZ=int(CNP[5:7])
    if iZ<1:
        return Falseø
    if LL!="02":
        if iZ>Zile[LL]:
            return False
    else:
        nZ=Zile[LL]
        if int(AA) % 4 == 0:
            if AA!="00":
                nZ+=1
            else:
                if S!='1' and S!=2:
                    nZ+=1
        if iZ>nZ:
            return False

    # Check JJ
    JJ=CNP[7:9]
    if JJ not in Judets.keys():
        return False

    # Check NNN
    NNN=CNP[9:12]
    if int(NNN)<1:
        return False

    # Check C
    C=CNP[12]
    if int(C)==Calculate_C(CNP):
        return True

    return False


def decorate(CNP):
    print(Componenta_S[CNP[0]])
    print("Data nasterii (ZZ/LL/AA): "+CNP[5:7]+"/"+CNP[3:5]+"/"+CNP[1:3])
    print("Judet: "+Judets[CNP[7:9]])
    print("Numar: "+CNP[9:12])



CNP=sys.argv[1]

if is_valid(CNP):
    print(CNP+" este valid")
    decorate(CNP)
else:
    print(CNP+" este nevalid")
