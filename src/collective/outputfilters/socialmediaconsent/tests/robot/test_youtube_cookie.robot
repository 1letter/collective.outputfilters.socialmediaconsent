# Start a single robot test
#
# Start the server
# WSGI_SERVER_HOST=localhost WSGI_SERVER_PORT=50003 robot-server collective.outputfilters.socialmediaconsent.testing.ACCEPTANCE_TESTING
#
# Start the test
# WSGI_SERVER_HOST=localhost WSGI_SERVER_PORT=50003 robot src/collective/outputfilters/socialmediaconsent/tests/robot/test_youtube_cookie.robot
#

** Settings ***

Resource    plone/app/robotframework/browser.robot
Resource    Products/CMFPlone/tests/robot/keywords.robot
Resource    keywords.robot

Library    Remote    ${PLONE_URL}/RobotRemote

Variables    variables.py

Test Setup    Run keywords    Plone Test Setup
Test Teardown    Run keywords    Plone Test Teardown

# Run robot tests in visual mode, not in headless mode
# switch BROWSER to chrome or firefox, the default is headlesschromium

*** Variables ***

${BROWSER}    chromium

${TEST_PAGE}    foo
${ANOTHER_TEST_PAGE}    bar
${COOKIENAME}    cos-youtobe-consent

*** Test Cases ***

Scenario: Cookie is not set
    Given a Page with YouTube video
     When I go to Page
     Then the cookie is unset
      and I see the consent box
      and I dont see the video

Scenario: Cookie setting - Consentbox is available
    Given a Page with YouTube video
     When I go to Page
      and I click consent
     Then the cookie is set
      and I see the video

Scenario: Cookie is set -
    Given a Page with YouTube video
      and another Page with YouTube video
     When I go to Page
      and I click consent
     Then the cookie is set
      and I see the video

     When I go to another Page
     Then I see the video

*** Keywords ***

# Given
a Page with YouTube video
    a logged-in manager
    Create content
    ...    type=Document
    ...    id=${TEST_PAGE}
    ...    title=Foo
    Go to  ${PLONE_URL}/${TEST_PAGE}/edit
    text inserted into wysiwyg
    Click    //button[@role="menuitem"]/span[contains(text(),"Insert")]
    Click    //div[@aria-label="Media..."]
    Click    //div[@role="tab" and contains(text(), "Embed")]
    Fill Text    //textarea[@data-mce-name="embed"]    ${YT_EMBEDDING_CODE}
    Click    //button[@data-mce-name="Save"]
    Click    //button[@id="form-buttons-save"]

another Page with YouTube video
    a logged-in manager
    Create content
    ...    type=Document
    ...    id=${ANOTHER_TEST_PAGE}
    ...    title=Bar
    Go to  ${PLONE_URL}/${ANOTHER_TEST_PAGE}/edit
    text inserted into wysiwyg
    Click    //button[@role="menuitem"]/span[contains(text(),"Insert")]
    Click    //div[@aria-label="Media..."]
    Click    //div[@role="tab" and contains(text(), "Embed")]
    Fill Text    //textarea[@data-mce-name="embed"]    ${YT_EMBEDDING_CODE}
    Click    //button[@data-mce-name="Save"]
    Click    //button[@id="form-buttons-save"]


# WHEN
I go to Page
    Go to  ${PLONE_URL}/${TEST_PAGE}

I click consent
    Click    //input[contains(@class,"socialmedia-consent-check")]

I go to another Page
    Go to  ${PLONE_URL}/${ANOTHER_TEST_PAGE}

# THEN
the cookie is unset
    ${cookie}=    Get Cookie    ${COOKIENAME}
    Should Be Equal    ${cookie.value}    0

the cookie is set
    ${cookie}=    Get Cookie    ${COOKIENAME}
    Should Be Equal    ${cookie.value}    1

I see the consent box
    Get Element Count    //div[contains(@class, "placeholder-socialmedia-consent")]    equal    1

I see the consent confirm check
    Get Element Count    //div[contains(@class, "socialmedia-consent-check")]    equal    1

I dont see the consent confirm check
    Get Element Count    //div[contains(@class, "socialmedia-consent-check")]    equal    0

I dont see the video
    Get Element Count    //div[contains(@class, "placeholder-socialmedia-consent")]/iframe    equal    0

I see the video
    Get Element Count    //div[contains(@class, "placeholder-socialmedia-consent")]/iframe    equal    1
