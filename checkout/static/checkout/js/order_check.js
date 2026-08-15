// Polling Django server for the created order if it exists and to repeat if it dosn't
const paymentIntent = document.getElementById("payment-intent");

// Use an async function to poll the server for the order status
async function checkOrder() {
    const response = await fetch(
        checkOrderUrl + "?payment_intent=" + paymentIntent.value
    );

    // Await the response and parse it as JSON (True or False)
    const data = await response.json();

    // If the order exists reload the page to be redirected and return
    if (data.ready) {
        window.location.reload();
        return;
    }

    // If we've made it here the order dosnt exist yet, so set a timeout to check again in 1 second
    setTimeout(checkOrder, 1000);
}

// Start the polling when the page loads
checkOrder();