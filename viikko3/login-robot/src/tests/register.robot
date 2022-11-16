*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  koira  koira123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  koira123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ko  koira123
    Output Should Contain  Username not valid

Register With Valid Username And Too Short Password
    Input Credentials  koira  k123
    Output Should Contain  Password not valid

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  koira  koirakoira
    Output Should Contain  Password not valid

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command