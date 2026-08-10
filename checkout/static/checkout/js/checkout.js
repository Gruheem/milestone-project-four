const form = document.getElementById("payment-form");
const continueBtn = document.getElementById("continue-button");
const payBtn = document.getElementById("pay-button");
const errorBox = document.getElementById("checkout-error");
let checkout;  // set once the Session exists, used by the submit handler below

// Event listener foor the continue button
continueBtn.addEventListener("click", async () => {
    errorBox.textContent = "";
    // Pack up the form data to send to the create_checkout_session view
    const formData = new FormData(form);

    // Call the create_checkout_session view to create a Stripe Checkout Session sending the payment form data to it
    const response = await fetch(checkoutSessionUrl, {
        method: "POST",
        body: formData,
    });
    const data = await response.json();

    // If there was an error creating the Session, display it to the user and return
    if (data.error) {
        if (typeof data.error === "string") {
            errorBox.textContent = data.error;
        } else {
            errorBox.textContent = "Please check the details above.";
        }
        return;
    }

    // Initialize the Stripe Checkout client with the returned client secret and mount the payment element
    checkout = stripe.initCheckout({
        clientSecret: data.clientSecret,
    });
    const paymentElement = checkout.createPaymentElement();
    paymentElement.mount("#checkout");

    // Disable the form fields and hide the continue button, show the pay button
    document.getElementById("details-fieldset").querySelectorAll("input").forEach(i => i.disabled = true);
    document.getElementById("delivery-fieldset").querySelectorAll("input, select").forEach(i => i.disabled = true);
    continueBtn.style.display = "none";
    payBtn.style.display = "inline-block";
});

// Event listener for the form submission
form.addEventListener("submit", async (e) => {
    e.preventDefault();
    if (!checkout) return;

    // Load the actions for the Checkout Session. Functions like a ready check befoe confirmation.
    const loadActionsResult = await checkout.loadActions();
    if (loadActionsResult.type !== "success") {
        errorBox.textContent = "Something went wrong loading checkout. Please refresh and try again.";
        return;
    }

    // Confirm the payment using the loaded actions
    const actionsResult = loadActionsResult; 
    const actions = actionsResult.actions;   
    const result = await actions.confirm();
    if (result.type === "error") {
        errorBox.textContent = result.error.message;
    }
});