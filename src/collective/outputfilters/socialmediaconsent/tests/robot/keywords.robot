*** Keywords ***

text inserted into wysiwyg
    Fill text to tinymce editor    Susi Sorglos and John Doe

embedded video inserted into wysiwyg '${CODE}'
    Click    //button[@role="menuitem"]/span[contains(text(),"Insert")]
    Click    //div[contains(text(), "Media...")]
    Click    //div[@role="tab" and contains(text(), "Embed")]
    Fill Text    //div[@class="tox-form"]//textarea[@data-mce-name="embed" or @class="tox-textarea"]   ${CODE}
    Click    //button[@data-mce-name="Save" or (@title="Save" and @class="tox-button")]
    Click    //button[@id="form-buttons-save"]

source code inserted into wysiwyg '${CODE}'
    Click    //button[@role="menuitem"]/span[contains(text(),"View")]
    Click    //div[contains(text(), "Source code")]
    Fill Text    //div[@class="tox-form"]//textarea[@data-mce-name="code" or @class="tox-textarea"]   ${CODE}
    Click    //button[@data-mce-name="Save" or (@title="Save" and @class="tox-button")]
    Click    //button[@id="form-buttons-save"]
