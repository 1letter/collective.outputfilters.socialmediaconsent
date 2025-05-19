# Start a single robot test
#
# Start the server
# WSGI_SERVER_HOST=localhost WSGI_SERVER_PORT=50003 robot-server collective.outputfilters.socialmediaconsent.testing.ACCEPTANCE_TESTING
#
# Start the test
# WSGI_SERVER_HOST=localhost WSGI_SERVER_PORT=50003 robot src/collective/outputfilters/socialmediaconsent/tests/robot/test_cookie_settings.robot
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

Scenario: Cookie activate on settings
    Given a Page with YouTube video
      and another Page with YouTube video
     When I go to Cookie Settings Page
     Then the cookie is unset

     When I go to Page
     Then the cookie is unset

     When I go to Cookie Settings Page
      and I click consent
     Then the cookie is set

     When I go to Page
     Then the cookie is set
      and I see the video

     When I go to another Page
     Then the cookie is set
      and I see the video
