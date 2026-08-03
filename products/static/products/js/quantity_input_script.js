document.addEventListener('DOMContentLoaded', function() {

    // Selecting by class name, so that we can use this script on multiple product pages if needed.
    const incButton = document.querySelectorAll('.increment-qty');
    const decButton = document.querySelectorAll('.decrement-qty');
    const qtyInput = document.querySelectorAll('.qty-input');

    // Checks the current value of the input and disables the increment or decrement buttons if the value is at the min or max.
    function updateButtonState() {
        let currentValue = parseInt(qtyInput.value);
        if (currentValue <= 1) {
            decButton.disabled = true;
        } else {
            decButton.disabled = false;
        }
        if (currentValue >= 99) {
            incButton.disabled = true;
        } else {
            incButton.disabled = false;
        }
    }
    
    // Increment Button function
    incButton.addEventListener('click', function() {
        let currentValue = parseInt(qtyInput.value);
        qtyInput.value = currentValue + 1;
        updateButtonState();
    });

    // Decrement Button function
    decButton.addEventListener('click', function() {
        let currentValue = parseInt(qtyInput.value);
        qtyInput.value = currentValue - 1;
        updateButtonState();
    });
    updateButtonState();
})