*** Settings ***
Documentation       ROBOCop HLKW checker

*** Settings ***
Library   OperatingSystem
Library   String
Library   Collections
#Resource    test/testCases.robot

*** Variables ***
${FileName}=  ccs2/RELIABILITY/TC_SWQUAL_CCS2_RELIABILITY_B2B_PA.robot
${Dir}      ccs2/
${Setup}    SETUP
${BOL}      ^
${QUOTE}    "
${EOL}      $

*** Test Cases ***
Check File
    Run  rm -f Imposters_v2.robot
    Run  rm -f testCases_v2.robot
    Run  echo "*** Settings ***" >> testCases_v2.robot
    Run  echo "" >> testCases.robot
    Run  echo "*** Test Cases ***" >> testCases_v2.robot
#    Run  echo "*** Keywords ***" >> test/testCases.robot

    ${Resources}=   Create List
    ${Keywords}=   Create List
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
                BREAK
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
                    Append To List    ${Keywords}    ${KeyWord}
                    ${Pattern}=  Catenate  ${BOL}${W}${EOL}
                    FOR  ${Resource}  IN  @{Resources}
                        ${CMD}=  Catenate  grep ${QUOTE}${Pattern}${QUOTE}  ${Resource}
                        ${contents}=   Run  ${CMD}
                        ${isFound}=    Run Keyword And Return Status    Should Not Be Empty    ${contents}
                        IF  ${isFound}
                            BREAK
                        END
                    END
                ELSE
                    IF  "${KeyWord}"!="${EMPTY}"
                        ${Args}=  Catenate  ${Args} ${W}
                    END
                END
            END
            IF  "${KeyWord}"!="${EMPTY}"
                Run  echo "${KeyWord}" >> testCases_v2.robot
                FOR  ${idx}  IN RANGE  0  4
                    Run  echo -n "${SPACE}" >> testCases_v2.robot
                END
                IF  not ${isFound}
#                    Log  ${KeyWord}  ERROR
                    Run  echo "< ${KeyWord} >" >> Imposters_v2.robot
                    Run  echo -n "\ \ [Arguments] ${Args}" >> Imposters_v2.robot
                    Run  echo '${Args}' >> Imposters_v2.robot
                    Run  echo "\ \ Keyword not defined, waiting for implementation." >> Imposters_v2.robot

                    Run  echo 'Should Be True\ \ ${FALSE}\ \ ${KeyWord}' >> testCases_v2.robot
                ELSE
                    Run  echo 'Should Be True\ \ ${TRUE}\ \ ${KeyWord}' >> testCases_v2.robot
#                    Log  ${KeyWord}
                END
                Run  echo "" >> testCases_v2.robot
            END
        ELSE
            ${Section}=  Get Substring  ${line}  0  5
            IF  "${Section}" == "${Setup}"
                ${inSETUP}=  Convert To Boolean  True
            END
            CONTINUE
        END
    END


#    FOR  ${Keyword}  IN  @{Keywords}
#        Run Keyword And Ignore Error  ${Keyword}
#    END
