*** Settings ***
Documentation       ROBOCop HLKW checker

*** Settings ***
Library   OperatingSystem
Library   String
Library   Collections

*** Variables ***
${FileName}=  ccs2/RELIABILITY/TC_SWQUAL_CCS2_RELIABILITY_B2B_PA.robot
${Count}    0
${Error}    0
${Dir}      ccs2/
${Setup}    SETUP
${BOL}      ^
${QUOTE}    "
${EOL}      $

*** Test Cases ***
Check File
    ${Resources}=   Create List
    ${contents}=   Grep File   ${FileName}   Resource
    @{lines}=      Split To Lines   ${contents}
    FOR   ${line}   IN   @{lines}
        ${Resource}=   Fetch From Right    ${line}   ${SPACE}
        ${Resource}=   Get Substring    ${Resource}   3
        ${Resource}=   Catenate    ${Dir}${Resource}
        Append To List    ${Resources}    ${Resource}
    END

    ${inSETUP}=  Convert To Boolean  False

    ${contents}=   Get File     ${FileName}    
    @{lines}=      Split To Lines   ${contents}
    FOR   ${line}   IN   @{lines}
        IF  ${inSETUP}  
            IF  "${line}"=="${EMPTY}"
                Exit For Loop
            END
            ${WS}=  Split String  ${line}  ${SPACE}${SPACE}
            ${KeyWord}=  Evaluate  ""
            ${Args}=  Evaluate  ""
            ${inFound}=  Convert To Boolean  False
            FOR  ${W}  IN  @{WS}
                IF  "${W}"=="${EMPTY}"
                    CONTINUE
                END
                IF  "${W}[0]"=="${SPACE}"
                    ${W}=  Get Substring  ${W}  1
                END
                ${UKW}=  Convert To Upper Case  ${W}
                IF  "${W}"=="${UKW}"
                    ${KeyWord}=  Evaluate  "${W}"
                    ${Pattern}=  Catenate  ${BOL}${W}${EOL}
                    FOR  ${Resource}  IN  @{Resources}
                        ${CMD}=  Catenate  grep ${QUOTE}${Pattern}${QUOTE}  ${Resource}
                        ${contents}=   Run  ${CMD}
                        ${isFound}=    Run Keyword And Return Status    Should Not Be Empty    ${contents}
                        IF  ${isFound}
                            Exit For Loop
                        END
                    END
                ELSE
                    IF  "${KeyWord}"!="${EMPTY}"
                        ${Args}=  Catenate  ${Args} ${W}
                    END
                END
            END
            IF  not ${isFound}
                IF  "${KeyWord}"!="${EMPTY}"
                    Log  ${KeyWord}  ERROR
                    Log  [Arguments] ${Args}  ERROR
                    Log  Keyword not defined, waiting for implementation.  ERROR
                END
            END
        ELSE
            ${Section}=  Get Substring  ${line}  0  5
            IF  "${Section}" == "${Setup}"
                ${inSETUP}=  Convert To Boolean  True
            END
            CONTINUE
        END
    END

