/**
* PHP Email Form Validation - v3.9
* URL: https://bootstrapmade.com/php-email-form/
* Author: BootstrapMade.com
*/
(function () {
  "use strict";

  function displayError(thisForm, errorMsg) {
  const errorElement = thisForm.querySelector('.error-message');
  if (errorElement) {
    errorElement.innerText = errorMsg;
    errorElement.classList.add('d-block');
  } else {
    alert(errorMsg);
  }
}


  let forms = document.querySelectorAll('.php-email-form');

  forms.forEach( function(e) {
    e.addEventListener('submit', function(event) {
      event.preventDefault();

      let thisForm = this;

      let action = thisForm.getAttribute('action');
      let recaptcha = thisForm.getAttribute('data-recaptcha-site-key');

      if( ! action ) {
        displayError(thisForm, 'The form action property is not set!');
        return;
      }
      thisForm.querySelector('.loading').classList.add('d-block');
      thisForm.querySelector('.error-message').classList.remove('d-block');
      thisForm.querySelector('.sent-message').classList.remove('d-block');

      let formData = new FormData( thisForm );

      if ( recaptcha ) {
        if(typeof grecaptcha !== "undefined" ) {
          grecaptcha.ready(function() {
            try {
              grecaptcha.execute(recaptcha, {action: 'php_email_form_submit'})
              .then(token => {
                formData.set('recaptcha-response', token);
                php_email_form_submit(thisForm, action, formData);
              })
            } catch(error) {
              displayError(thisForm, error);
            }
          });
        } else {
          displayError(thisForm, 'The reCaptcha javascript API url is not loaded!')
        }
      } else {
        php_email_form_submit(thisForm, action, formData);
      }
    });
  });

  function php_email_form_submit(thisForm, action, formData) {
    fetch(action, {
      method: 'POST',
      body: formData,
      headers: {'X-Requested-With': 'XMLHttpRequest'},
      url: '/contact/contact_form'
    })
    .then(response => {
  if (response.ok) {
    return response.json();
  } else {
    throw new Error(`${response.status} ${response.statusText} ${response.url}`);
  }
})
.then(data => {
  thisForm.querySelector('.loading').classList.remove('d-block');

  if (data.success) {
    thisForm.querySelector('.sent-message').classList.add('d-block');
    thisForm.querySelector('.sent-message').innerHTML = data.message || "Your message has been sent successfully.";
    thisForm.querySelector('.error-message').classList.remove('d-block');
    thisForm.reset();
  } else {
    displayError(thisForm, data.message || 'Form submission failed.');
  }
})

        .catch((error) => {
          displayError(thisForm, error.message || error);
        });

  }

})();

