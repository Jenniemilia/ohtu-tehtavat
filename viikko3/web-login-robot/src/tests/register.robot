*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  jenni
    Set Password  jenni000
    Set Password Confirmation  jenni000
    Submit Credentials  
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  q
    Set Password  jenni000
    Set Password Confirmation  jenni000
    Submit Credentials
    Registration Should Fail With Message  Username Too Short


*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}   

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}


Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password  ${password}


Submit Credentials
    Click Button  Register
