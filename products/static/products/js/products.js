document.addEventListener('DOMContentLoaded', function() {
    const filterBtn = document.getElementById('filter-button');
    const attributeList = document.getElementById('attribute-list');

    filterBtn.addEventListener('click', function() {
        if (window.innerWidth < 992) {
            attributeList.classList.toggle('d-none');
        }
    });
})