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

*** Test Cases ***

Scenario: Cookie is not set
    Given a logged-in manager
      and a Page with YouTube video
     When I go to Page
     Then the cookie is unset
      and I see the consent box
      and I dont see the video

Scenario: Cookie setting - Consentbox is available
    Given a logged-in manager
      and a Page with YouTube video
     When I go to Page
      and I click consent youtube
     Then the cookie is set
      and I see the video

Scenario: Cookie is set - Video on the other page is present
    Given a logged-in manager
      and a Page with YouTube video
      and another Page with YouTube video
     When I go to Page
      and I click consent youtube
     Then the cookie is set
      and I see the video

     When I go to another Page
     Then I see the video

*** Keywords ***

# GIVEN

a Page with YouTube video
    Create content
    ...    type=Document
    ...    id=${TEST_PAGE}
    ...    title=Foo
    Go to  ${PLONE_URL}/${TEST_PAGE}/edit
    text inserted into wysiwyg
    embedded video inserted into wysiwyg '${YT_EMBEDDING_CODE}'

another Page with YouTube video
    Create content
    ...    type=Document
    ...    id=${ANOTHER_TEST_PAGE}
    ...    title=Bar
    Go to  ${PLONE_URL}/${ANOTHER_TEST_PAGE}/edit
    text inserted into wysiwyg
    embedded video inserted into wysiwyg '${YT_EMBEDDING_CODE}'

# WHEN

I go to Page
    Go to  ${PLONE_URL}/${TEST_PAGE}

I go to another Page
    Go to  ${PLONE_URL}/${ANOTHER_TEST_PAGE}

the cookie is unset
    ${cookie}=    Get Cookie    ${COOKIENAME_YOUTUBE}
    Should Be Equal    ${cookie.value}    0

I click consent youtube
    Click    //input[contains(@class,"socialmedia-consent-check-youtube")]

# THEN

I see the consent box
    Get Element Count    //div[contains(@class, "placeholder-socialmedia-consent-youtube")]    equal    1

I see the consent confirm check
    Get Element Count    //div[contains(@class, "socialmedia-consent-check-youtube")]    equal    1

I dont see the consent confirm check
    Get Element Count    //div[contains(@class, "socialmedia-consent-check-youtube")]    equal    0

I see the video
    Get Element Count    //div[contains(@class, "placeholder-socialmedia-consent")]/iframe    equal    1

I dont see the video
    Get Element Count    //div[contains(@class, "placeholder-socialmedia-consent")]/iframe    equal    0

the cookie is set
    ${cookie}=    Get Cookie    ${COOKIENAME_YOUTUBE}
    Should Be Equal    ${cookie.value}    1
