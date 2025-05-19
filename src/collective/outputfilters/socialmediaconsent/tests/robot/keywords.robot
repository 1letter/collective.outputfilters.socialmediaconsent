*** Keywords ***

text inserted into wysiwyg
    Fill text to tinymce editor    Susi Sorglos and John Doe

I go to Cookie Settings Page
    Go to  ${PLONE_URL}/cos-cookie-settings

the cookie is unset
    ${cookie}=    Get Cookie    ${COOKIENAME}
    Should Be Equal    ${cookie.value}    0

the cookie is set
    ${cookie}=    Get Cookie    ${COOKIENAME}
    Should Be Equal    ${cookie.value}    1

a Page with YouTube video
    a logged-in manager
    Create content
    ...    type=Document
    ...    id=${TEST_PAGE}
    ...    title=Foo
    Go to  ${PLONE_URL}/${TEST_PAGE}/edit
    text inserted into wysiwyg
    Click    //button[@role="menuitem"]/span[contains(text(),"Insert")]
    Click    //div[contains(text(), "Media...")]
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
    Click    //div[contains(text(), "Media...")]
    Click    //div[@role="tab" and contains(text(), "Embed")]
    Fill Text    //textarea[@data-mce-name="embed"]    ${YT_EMBEDDING_CODE}
    Click    //button[@data-mce-name="Save"]
    Click    //button[@id="form-buttons-save"]

I go to another Page
    Go to  ${PLONE_URL}/${ANOTHER_TEST_PAGE}

I click consent
    Click    //input[contains(@class,"socialmedia-consent-check")]

I go to Page
    Go to  ${PLONE_URL}/${TEST_PAGE}

I dont see the video
    Get Element Count    //div[contains(@class, "placeholder-socialmedia-consent")]/iframe    equal    0

I see the video
    Get Element Count    //div[contains(@class, "placeholder-socialmedia-consent")]/iframe    equal    1