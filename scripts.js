

    document.addEventListener('DOMContentLoaded', function() {
      const hamburger = document.querySelector('.hamburger');
      const navMenu = document.querySelector('.nav-menu');
      const navItems = document.querySelectorAll('.nav-item');

      hamburger.addEventListener('click', function() {
        navMenu.classList.toggle('active');
      });

      navItems.forEach(item => {
        item.addEventListener('click', function(e) {
          if (window.innerWidth <= 768) {
            if (e.target.classList.contains('nav-link') && e.target.nextElementSibling) {
              e.preventDefault();
              this.classList.toggle('active');
            }
          }
        });
      });

      window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
          navMenu.classList.remove('active');
          navItems.forEach(item => item.classList.remove('active'));
        }
      });

      document.addEventListener('click', function(e) {
        if (!e.target.closest('.nav-menu') && !e.target.closest('.hamburger')) {
          navMenu.classList.remove('active');
          navItems.forEach(item => item.classList.remove('active'));
        }
      });
    });

