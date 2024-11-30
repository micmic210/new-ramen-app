
// Welcome section 
// Smooth scroll to sections
function scrollToSection(sectionId) {
    document.querySelector(sectionId).scrollIntoView({ behavior: 'smooth' });
  
    // Remove active class from all buttons
    document.querySelectorAll('.cta-btn').forEach(btn => btn.classList.remove('active'));
  
    // Add active class to clicked button
    if (sectionId === '#menu') {
      document.querySelector('.cta-green').classList.add('active');
    } else if (sectionId === '#reservation') {
      document.querySelector('.cta-orange').classList.add('active');
    }
  }
  
  // JavaScript to handle Learn More button click
  document.addEventListener("DOMContentLoaded", () => {
    const learnMoreButton = document.getElementById("learnMoreButton");
  
    if (learnMoreButton) {
      learnMoreButton.addEventListener("click", () => {
        window.location.href = "philosophy.html"; // Navigate to the target page
      });
    }
  });
  
  
  // Menu Section
  // Wait for the DOM to load
  document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".menu-btn");
    const menuCategories = document.querySelectorAll(".menu-category");
  
    // Function to show the selected category
    const showCategory = (targetId) => {
      // If "All" is clicked, show all categories
      if (targetId === "#all") {
        menuCategories.forEach((category) => {
          category.classList.remove("d-none");
        });
      } else {
        // Hide all categories first
        menuCategories.forEach((category) => {
          category.classList.add("d-none");
        });
        // Show the selected category
        const targetCategory = document.querySelector(targetId);
        if (targetCategory) {
          targetCategory.classList.remove("d-none");
        }
      }
    };
  
    // Add click event listeners to buttons
    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        // Remove the "active" class from all buttons
        buttons.forEach((btn) => btn.classList.remove("active"));
        // Add the "active" class to the clicked button
        button.classList.add("active");
        // Show the selected category
        const targetId = button.getAttribute("data-target");
        showCategory(targetId);
      });
    });
  
    // Ensure only "All" button is active on page load
    buttons.forEach((button) => {
      const targetId = button.getAttribute("data-target");
      if (targetId === "#all") {
        button.classList.add("active");
      } else {
        button.classList.remove("active");
      }
    });
  
    // Show "All" category by default
    showCategory("#all");
  });
  