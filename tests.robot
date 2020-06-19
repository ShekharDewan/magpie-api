*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
User can view listings by Designer
    open browser    https://google.ca/  firefox 
    input text  name:q  hello
    click element  id:viewport
    click button  xpath://html/body/div/div[3]/form/div[2]/div[1]/div[3]/center/input[1]
    close browser

*** Keywords ***