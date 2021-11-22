*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jenni  jennikoodaa123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  jenni  jennikoodaa2

Register With Too Short Username And Valid Password
    Input Credentials  je  jennikoodaa2

Register With Valid Username And Too Short Password
    Input Credentials  jenni  sala

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  jenni  salasanani

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command