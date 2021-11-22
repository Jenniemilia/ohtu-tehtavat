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
    Registration Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  jenni
    Set Password  koodi
    Set Password Confirmation  koodi
    Submit Credentials
    Registration Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  jenni
    Set Password  koodari00
    Set Password Confirmation  00koodari
    Submit Credentials
    Registration Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username  jenni
    Set Password  koodari11
    Set Password Confirmation  koodari11
    Submit Credentials
    Registration Should Succeed
    Go To Login Page
    Set Username  jenni
    Set Password  koodari11
    Submit Login  
    Login Should Succeed    

Login After Failed Registration
    Set Username  jenni
    Set Password  koodari11
    Set Password Confirmation  kood
    Submit Credentials
    Registration Should Fail With Message  Passwords don't match
    Go To Login Page
    Set Username  jenni
    Set Password  koodari11
    Submit Login
    Login Should Fail With Message  Invalid username or password



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
    Input Password  password_confirmation  ${password}


Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}


