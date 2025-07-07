document.addEventListener('DOMContentLoaded', function() {
    // Developer Modal
    const addDeveloperBtn = document.getElementById('add-developer-btn');
    const developerModal = document.getElementById('add-developer-modal');
    const closeDeveloperModal = developerModal.querySelector('.close-btn');

    if (addDeveloperBtn) {
        addDeveloperBtn.onclick = function() {
            developerModal.style.display = 'block';
        }
    }

    if (closeDeveloperModal) {
        closeDeveloperModal.onclick = function() {
            developerModal.style.display = 'none';
        }
    }

    // Client Modal
    const addClientBtn = document.getElementById('add-client-btn');
    const clientModal = document.getElementById('add-client-modal');
    const closeClientModal = clientModal.querySelector('.close-btn');

    if (addClientBtn) {
        addClientBtn.onclick = function() {
            clientModal.style.display = 'block';
        }
    }

    if (closeClientModal) {
        closeClientModal.onclick = function() {
            clientModal.style.display = 'none';
        }
    }

    // Close modal if user clicks outside of it
    window.onclick = function(event) {
        if (event.target == developerModal) {
            developerModal.style.display = 'none';
        }
        if (event.target == clientModal) {
            clientModal.style.display = 'none';
        }
    }
});