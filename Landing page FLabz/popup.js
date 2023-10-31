document.addEventListener('DOMContentLoaded', function() {
    var contact = document.getElementById('contact');
    var contactForm = document.getElementById('contactForm');
  
    if (contact && contactForm) {
      contact.addEventListener('click', function() {
        if (contactForm.style.display === 'none' || !contactForm.style.display) {
          contactForm.style.display = 'block';
          document.querySelector('.overlay').style.display = 'block';
        } else {
          contactForm.style.display = 'none';
          document.getElementById('contactForm').style.display = 'none';
          document.querySelector('.overlay').style.display = 'none';
        }
      });
  
      // Initially hide the contactForm
      contactForm.style.display = 'none';
    }
  });
  
  