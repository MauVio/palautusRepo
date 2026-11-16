*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  Moikka  kalle123
    Output Should Contain  New user registered


Register With Already Taken Username And Valid Password
    Input Credentials  kalle  moikka123
    Output Should Contain  User with username kalle already exists


Register With Too Short Username And Valid Password
    Input Credentials  m  moi123
    Output Should Contain  Username should be atleat 3 chars long


Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  mäöäöä  moi123
    Output Should Contain  Username can only contain letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  heippa  a234567
    Output Should Contain  Password should be atleast 8 chars long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  heippa  abcdefghija
    Output Should Contain  Password should have letters and numbers
    
*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
  