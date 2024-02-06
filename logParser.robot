*** Settings ***
Documentation       Robot log parser

*** Settings ***
Library   OperatingSystem
Library   String
Library   DateTime
Library   Collections
Library   pythonCode.py

*** Variables ***
${AppDict}=  Create Dictionary
${name}  application_
${Year}  2023_
${Count}    0
${Error}    0

*** Test Cases ***
Read File
    ${AppDict}=   Create Dictionary
    ${contents}=   Grep File  ~/Downloads/logcat_applications.txt    ActivityTaskManager: START u0
    @{lines}=      Split To Lines   ${contents}
    FOR   ${line}   IN   @{lines}
        ${App}=   Fetch From Right   ${line}   cmp=
        ${App}=   Fetch From Left   ${App}   /
        ${Started}=   Get Substring   ${line}   0    18
        ${Count}=  Evaluate  ${Count}+1
        ${Key}=  Catenate   ${name}${Count}
        ${DApp}=  Create Dictionary  app_path  ${App}  ts_app_started  ${Started}  ts_app_closed  ${Started}  lifespan  0
        Set To Dictionary   ${AppDict}   ${Key}   ${DApp}
    END

    ${contents}=   Grep File  ~/Downloads/logcat_applications.txt    Layer: Destroyed ActivityRecord
    @{lines}=      Split To Lines   ${contents}
    FOR   ${line}   IN   @{lines}
        FOR  ${App}  IN  @{AppDict}
            ${contains}=    Run Keyword And Return Status    Should Contain    ${line}    ${AppDict['${App}']['app_path']}
            IF  ${contains} 
                ${End}=   Get Substring   ${line}   0    18
                Set To Dictionary  ${AppDict['${App}']}  ts_app_closed  ${End}
                ${CEnd}=  Catenate  ${Year}${End}
                ${Date1}=   Convert Date   ${CEnd}
                ${CStart}=  Catenate  ${Year}${AppDict['${App}']['ts_app_started']}
                ${Date2}=   Convert Date   ${CStart}
                ${TS}=  Subtract Date From Date  ${Date1}  ${Date2}
                Set To Dictionary  ${AppDict['${App}']}  lifespan  ${TS}
            END
        END
    END

#    ${contents}=   Get File         ~/Downloads/logcat_applications.txt
#    @{lines}=      Split To Lines   ${contents}
#    FOR   ${line}   IN   @{lines}
#        ${contains}=    Run Keyword And Return Status    Should Contain    ${line}    ActivityTaskManager: START u0
#        IF  ${contains} 
#            ${App}=   Fetch From Right   ${line}   cmp=
#            ${App}=   Fetch From Left   ${App}   /
#            ${Started}=   Get Substring   ${line}   0    18
#            ${Count}=  Evaluate  ${Count}+1
#            ${Key}=  Catenate   ${name}${Count}
#            ${DApp}=  Create Dictionary  app_path  ${App}  ts_app_started  ${Started}  ts_app_closed  ${Started}  lifespan  0
#            Set To Dictionary   ${AppDict}   ${Key}   ${DApp}
#        ELSE
#            ${contains}=    Run Keyword And Return Status    Should Contain    ${line}    Layer: Destroyed ActivityRecord
#            IF  ${contains} 
#                FOR  ${App}  IN  @{AppDict}
#                    ${contains}=    Run Keyword And Return Status    Should Contain    ${line}    ${AppDict['${App}']['app_path']}
#                    IF  ${contains} 
#                        ${End}=   Get Substring   ${line}   0    18
#                        Set To Dictionary  ${AppDict['${App}']}  ts_app_closed  ${End}
#                        ${CEnd}=  Catenate  ${Year}${End}
#                        ${Date1}=   Convert Date   ${CEnd}
#                        ${CStart}=  Catenate  ${Year}${AppDict['${App}']['ts_app_started']}
#                        ${Date2}=   Convert Date   ${CStart}
#                        ${TS}=  Subtract Date From Date  ${Date1}  ${Date2}
#                        Set To Dictionary  ${AppDict['${App}']}  lifespan  ${TS}
#                        BREAK
#                    END
#                END
#            END
#        END
#    END
    
    writeYaml  ${AppDict}

    ${mess}=  Catenate  Found  ${Count}  applications  
     log  ${mess}  WARN
    FOR  ${App}  IN  @{AppDict}
        IF  ${AppDict['${App}']['lifespan']} > 30.000
            ${mess}=  Catenate  ${App}  : lifespan (
            ${mess}=  Catenate  ${mess}  ${AppDict['${App}']['lifespan']}
            ${mess}=  Catenate  ${mess}  ) is greater than 30.000 seconds
            log  ${mess}  WARN
            ${Error}=  Evaluate  ${Error}+1
        END
    END
    ${Err}=  Evaluate  ${Error}/${Count}*100
    IF  ${Err} > 25
        FAIL  More than 25% of applications have a lifespan grater thant 30.000 secondd
    END

