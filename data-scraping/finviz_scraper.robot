*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary
Library    BuiltIn
Library    OperatingSystem

*** Variables ***
${URL}    https://finviz.com/quote.ashx?t=SPY&p=d
${BROWSER}    firefox
${HEADLINE_SELECTOR}    //a[@class="tab-link-news"]
${AGREE_BUTTON_SELECTOR}    //span[text()="AGREE"]
${OUTPUT_FILE}    headlines.txt

*** Test Cases ***
Scrape S&P 500 Financial Headlines
    Open Browser To Finviz
    Accept Cookies
    Get All Headlines
    Close Browser

*** Keywords ***
Open Browser To Finviz
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains Element    ${AGREE_BUTTON_SELECTOR}    timeout=10s

Accept Cookies
    Wait Until Page Contains Element    ${AGREE_BUTTON_SELECTOR}    timeout=10s
    Click Element    ${AGREE_BUTTON_SELECTOR}
    Log    "Cookies accepted"

Get All Headlines
    @{headlines}    Get WebElements    ${HEADLINE_SELECTOR}
    ${headline_count}    Get Length    ${headlines}    # Correct way to get the length of the list
    Log    "Found ${headline_count} headlines"   # Log the number of found headlines

    FOR    ${headline}    IN    @{headlines}
        ${headline_text}    Get Text    ${headline}
        ${headline_link}    Get Element Attribute    ${headline}    href
        Log    ${headline_text} - ${headline_link}
        Append To File    ${OUTPUT_FILE}    ${headline_text} - ${headline_link}\n
        Log    "Processed headline: ${headline_text}"   # Log after each headline is processed
    END
