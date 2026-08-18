document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.toast').forEach(function(toast) {
        new bootstrap.Toast(toast, {
            autohide: false
        }).show();
    });

    const searchBtn = document.getElementById('search-btn')
    const searchInput = document.getElementById('search-input')
    searchBtn.addEventListener('click', function() {
        searchInput.classList.remove('d-none');
        searchInput.focus();
        // Change the button type to 'submit'. A delay of 0 just brings it to the back of the event queue, 
        // allowing the click event to finish before changing the type.
        setTimeout(() => {
            searchBtn.type = 'submit';
        }, 0);
    });
});