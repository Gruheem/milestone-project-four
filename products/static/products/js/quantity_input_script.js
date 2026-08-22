document.addEventListener('DOMContentLoaded', function() {

    // Returns a list of all the button with the class...
    const incButtons = document.querySelectorAll('.increment-qty');
    const decButtons = document.querySelectorAll('.decrement-qty');


    // Checks the value of the input and disables the increment or decrement buttons if the value is at the min or max. Given arguments for reusability
    function updateButtonState(input, incButton, decButton) {
        let currentValue = parseInt(input.value);
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
    
    // Iterates through the increment button list
    incButtons.forEach(button => {
        
        button.addEventListener('click', function() {
            // Define our inputs to alter and feed to the updateButtonState function
            const form = this.closest('.form');
            const input = form.querySelector('.qty-input');
            const decButton = form.querySelector('.decrement-qty');

            // Get the current value of the input
            let currentValue = parseInt(input.value);

            // Defensive Programming incase the check in the updateButtonState function fails
            if (currentValue < 99) {
                // Increment the value of the input by 1
                input.value = currentValue + 1;
            }

            updateButtonState(input, this, decButton);

            if (form.classList.contains('update-form')) {
                form.submit();
            }
        });
    });
    

    // Iterates through the decrement button list
    decButtons.forEach(button => {
        
        button.addEventListener('click', function() {
            // Define our inputs to alter and feed to the updateButtonState function
            const form = this.closest('.form');
            const input = form.querySelector('.qty-input');
            const incButton = form.querySelector('.increment-qty');

            // Get the current value of the input
            let currentValue = parseInt(input.value);

            // Defensive Programming incase the check in the updateButtonState function fails
            if (currentValue > 1) {
                // Decrement the value of the input by 1
                input.value = currentValue - 1;
            }

            updateButtonState(input, incButton, this);

            if (form.classList.contains('update-form')) {
                form.submit();
            }
        });
    });

    // Iterates through all the quantity inputs to set their state on page load
    document.querySelectorAll('.qty-input').forEach(input => {
        const form = input.closest('.form');
        const incButton = form.querySelector('.increment-qty');
        const decButton = form.querySelector('.decrement-qty');
        updateButtonState(input, incButton, decButton);
    });
});