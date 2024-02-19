#!/usr/bin/env python3

import requests
import json

URL="https://rickandmortyapi.com/api/"

def ex_1():
    result=requests.get(URL+'character/?name=Rick Sanchez')
    Dict=json.loads(result.text)
    print('Character id of Rick Sanchez is '+str(Dict['results'][0]['id']))


def ex_2():
    result=requests.get(URL+'character/?name=Rick Sanchez')
    Dict=json.loads(result.text)
    print('Current status of Rick Sanchez is '+str(Dict['results'][0]['status']))
    print('Current location of Rick Sanchez is '+str(Dict['results'][0]['location']['name']))
    result=requests.get(URL+'character/?name=Morty Smith')
    Dict=json.loads(result.text)
    print('Current status of Morty Smith is '+str(Dict['results'][0]['status']))
    print('Current location of Morty Smith is '+str(Dict['results'][0]['location']['name']))


def ex_3():
    result=requests.get(URL+'character/?name=Gene')
    Dict=json.loads(result.text)
    EP=[]
    for APP in Dict['results']:
        if APP['name']=='Gene':
            location=APP['location']['name']
            for episode in APP['episode']:
                # name=requests.get(APP['url'])[0]['name'])
                EP.append(episode)
            break
    print('Location of Gene is '+location)
    print('Gene appears in '+str(EP))


def ex_4():
    result=requests.get(URL+'location/?name=Narnia Dimension')
    Dict=json.loads(result.text)
    LNames=[]
    for UD in Dict['results'][0]['residents']:
        CResult=requests.get(UD)
        CDict=json.loads(CResult.text)
        name=CDict['name']
        status=CDict['status']
        if status=='Alive':
            LNames.append(name)
    print(LNames)


def ex_5():
    print('Episode 28: Characters with "Rick" in their name')
    result=requests.get(URL+'episode/28')
    Dict=json.loads(result.text)
    LNames=[]
    for UD in Dict['characters']:
        CResult=requests.get(UD)
        CDict=json.loads(CResult.text)
        name=CDict['name']
        if 'Rick' in name:
            LNames.append(name)
    print(LNames)


def ex_6():
    print('Episode 29: Characters who are not alive')
    result=requests.get(URL+'episode/29')
    Dict=json.loads(result.text)
    LNames=[]
    for UD in Dict['characters']:
        CResult=requests.get(UD)
        CDict=json.loads(CResult.text)
        name=CDict['name']
        status=CDict['status']
        if status!='Alive':
            LNames.append(name+" ("+status+")")
    print(LNames)


def ex_7():
    print('Species types that appear in Season 3')
    LSpecies={}
    for EP in range(22, 32):
        result=requests.get(URL+'episode/'+str(EP))
        Dict=json.loads(result.text)
        for UD in Dict['characters']:
            CResult=requests.get(UD)
            CDict=json.loads(CResult.text)
            Type=CDict['type']
            Species=CDict['species']
            Name=CDict['name']
            if Species not in LSpecies.keys():
                LSpecies[Species]=[]
                DType={}
                DType['type']=Type
                DType['names']=[]
                DType['names'].append(Name)
                LSpecies[Species].append(DType)
            else:
                TFound=False
                for DType in LSpecies[Species]:
                    if DType['type']==Type:
                        if Name not in DType['names']:
                            DType['names'].append(Name)
                        TFound=True
                        break
                if not TFound:
                    DType={}
                    DType['type']=Type
                    DType['names']=[]
                    DType['names'].append(Name)
                    LSpecies[Species].append(DType)
    for Species in LSpecies.keys():
        if Species!='Human':
            for DType in LSpecies[Species]:
                if DType['type']=='':
                    for Name in DType['names']:
                        print('Species='+Species+', Name='+Name)
                else:
                    for Name in DType['names']:
                        print('Species='+Species+', Type='+DType['type']+', Name='+Name)
        



print('-1-')
ex_1()
print('')
print('-2-')
ex_2()
print('')
print('-3-')
ex_3()
print('')
print('-4-')
ex_4()
print('')
print('-5-')
ex_5()
print('')
print('-6-')
ex_6()
print('')
print('-7-')
ex_7()
print('')
