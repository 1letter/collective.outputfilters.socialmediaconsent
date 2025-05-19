const SHOW = "1";
const HIDE = "0";

let Consent = {
  youtube: {
    value : HIDE,
    name : "cos-youtube-consent",
    cbx : "check-youtube"
  },
  third_party: {
    value : HIDE,
    name : "cos-thitdparty-consent",
    cbx : "check-thirdparty"
  },
}

window.addEventListener("load", cos_init);

function cos_init(event){

  // initialize cookiehandling
  cookiehandling()

  // check if cookie exists, then replace
  // replace all placeholders with the markup from the contentfilter
  update_markup()
}

function cookiehandling(){

  // add click events to cookie consent checkboxes
  let checkboxes = document.querySelectorAll("input.socialmedia-consent-check");
  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("click", set_consent);
  });

  Object.keys(Consent).forEach((key) => {
    if (
      document.cookie.split(";").some((item) => item.trim().startsWith(Consent[key].name+"="))
    ){

      // Cookie exist
      if (document.cookie.split(";").some((item) => item.includes(Consent[key].name + "=" + SHOW))) {
        Consent[key].value = SHOW;
      } else{
        Consent[key].value = HIDE;
      }

    } else{
      // Cookie don't exist
      // set the cookie with default value (HIDE)
      // this disable the rendering of youtube video iframes
      Consent[key].value = HIDE;
      document.cookie = Consent[key].name+"="+HIDE+";Secure;path=/";
    }

    // handle the checkboxes, if the cookie is set, enable the checkboxes
    checkboxes.forEach((checkbox) => {
      if( checkbox.id == Consent[key].cbx && Consent[key].value == SHOW){
        checkbox.checked = true
      }
      if( checkbox.id == Consent[key].cbx && Consent[key].value == HIDE){
        checkbox.checked = false
      }
    });

  });
}

function set_consent(event){
  let cbx_id = event.target.id;
  let checked = event.target.checked;

  Object.keys(Consent).forEach((key) => {
    if(cbx_id == Consent[key].cbx){
      if(checked === true){
        show(Consent[key])
      } else{
        hide(Consent[key])
      }
    }
  });

  update_markup()
}

function show(consent){
  consent.value = SHOW;
  document.cookie = consent.name+"="+consent.value+";Secure;path=/";
}

function hide(consent){
  consent.value = HIDE;
  document.cookie = consent.name+"="+consent.value+";Secure;path=/";
}

function update_markup(){

  let markupElements = document.querySelectorAll("div[data-cos]");
  markupElements.forEach((markupElement) => {
    let options = JSON.parse(markupElement.dataset.cos)
    let old_markup = markupElement.innerHTML
    let new_markup = options.markup
    let consent_type = options.consent
    Object.keys(Consent).forEach((key) => {
      if(key == consent_type && Consent[key].value == SHOW){
        markupElement.innerHTML = new_markup
        options.markup = old_markup
      }
    });
  });
}

function parseHTML(markup_as_string){
  var wrapper= document.createElement('div');
  wrapper.innerHTML= markup_as_string;
  return wrapper.firstChild
}