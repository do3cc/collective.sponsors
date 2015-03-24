*** Keywords ***
I am logged in as '${role}'
    Enable autologin as  ${role}

I see a link to create a sponsor folder
    Element Should Be Visible  css=a.create-sponsor-folder

I click the createa sponsor folder
    Click Link css=a.create-sponsor-folder

I add a new sponsor
    Add link  Mastersponsor

I go to the frontpage
    Go To  ${PLONE_URL}

I see the sponsor
    Element Should Be Visible css=a.sponsor

I do not see the sponsor folder in the top level navigation
    Element Should Not Be Visible id="sponsor"
