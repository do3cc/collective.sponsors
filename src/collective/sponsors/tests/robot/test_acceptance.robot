# ============================================================================
# EXAMPLE ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.sponsors -t test_example.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.sponsors.testing.COLLECTIVE_SPONSORS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/collective/sponsors/tests/robot/test_example.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot
Resource  collective/sponsors/tests/robot/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As an admin, I want to be able to quickly add the sponsors folder and sponsors to a new site.
    Given I am logged in as 'Manager'
     Then I see A link to create a sponsor folder
     When I click the create a sponsor folder
     Then I am in the sponsor folder
     When I add a new sponsor
     When I go to the frontpage
     Then I see the sponsor
     Then I do not see the sponsor folder in the top level navigation

Scenario: As a visitor, I want to see the sponsors
    Given I go to the frontpage
     Then I see the sponsor
     Then I do not see the sponsor folder in the top level navigation


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a login form
  Go To  ${PLONE_URL}/login_form
  Wait until page contains  Login Name
  Wait until page contains  Password


# --- WHEN -------------------------------------------------------------------

I enter valid credentials
  Input Text  __ac_name  admin
  Input Text  __ac_password  secret
  Click Button  Log in


# --- THEN -------------------------------------------------------------------

I am logged in
  Wait until page contains  You are now logged in
  Page should contain  You are now logged in
