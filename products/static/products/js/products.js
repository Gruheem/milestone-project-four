document.addEventListener('DOMContentLoaded', function() {
    const filterBtn = document.getElementById('filter-button');
    const attributeList = document.getElementById('attribute-list');

    filterBtn.addEventListener('click', function() {
        if (window.innerWidth < 992) {
            attributeList.classList.toggle('d-none');
        }
    });

    // const sortSelect = document.getElementById('sort-select');
    // console.log(sortSelect);
    // sortSelect.addEventListener('change', function() {
    //     if (this.value === 'reset') {
    //         this.classList.add('placeholder');
    //     } else {
    //         this.classList.remove('placeholder');
    //     }
    // });

})