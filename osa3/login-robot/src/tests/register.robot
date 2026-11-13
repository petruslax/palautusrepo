*** Settings ***
Resource  resource.robot  

*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Input Credentials
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input New Command And Input Credentials
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  aa  kalle123
    Output Should Contain  Username must be at least 3 letters

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  kalle1  kalle123
    Output Should Contain  Username invalid, use only letters a-z

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  kalle  kalle12
    Output Should Contain  Password must be at least 8 letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  kalle  kallekoo
    Output Should Contain  Password must contain numbers or special characters

*** Keywords ***
Input New Command And Input Credentials
    Input New Command
    Input Credentials  kalle  kalle123