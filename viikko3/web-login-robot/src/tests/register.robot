*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Open Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  nimi
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Register User
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Register User
    Register Should Fail With Message  Username not valid

Register With Valid Username And Too Short Password
    Set Username  koira
    Set Password  ka23
    Set Password Confirmation  ka123
    Register User
    Register Should Fail With Message  Password not valid

Register With Nonmatching Password And Password Confirmation
    Set Username  kissa
    Set Password  kalle123
    Set Password Confirmation  kalle12
    Register User
    Register Should Fail With Message  Password confirmation does not match

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register User
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Open Register Page
    Go To Register Page
    Register Page Should Be Open