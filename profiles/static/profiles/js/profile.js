console.log('profile.js loaded');

document.addEventListener('DOMContentLoaded', function() {
    // sets text colour of Country input field
    const countrySelect = document.getElementById('id_default_country');
    let countrySelected = document.getElementById('id_default_country').value;
    if (!countrySelected) {
        countrySelect.style.color = 'var(--placeholder-colour)';
    }
    countrySelect.addEventListener('change', function() {
        countrySelected = this.value;
        if (!countrySelected) {
            this.style.color = 'var(--text-colour-muted)';
        } else {
            this.style.color = 'var(--placeholder-colour)';
        }
    });
})