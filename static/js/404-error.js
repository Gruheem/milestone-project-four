document.addEventListener('DOMContentLoaded', function() {
    // Listener for back button on 404 page
    const backButton = document.getElementById('back-button');
    backButton.addEventListener('click', function() {
        window.history.back();
    });
});