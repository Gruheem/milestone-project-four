console.log('script loaded')
// Waiting for the DOM to load ensures our filter-panel exists at the point our script runs and it is selected.
document.addEventListener('DOMContentLoaded', function() {
    // Get our div with our checkboxes in it.
    const filterPanel = document.getElementById('filter-panel');
    
    // Adds Listener on our selected element
    filterPanel.addEventListener('change', function(event) {
        // If what changed in this div was not a checkbox exit the function.
        if (event.target.type !== 'checkbox') return;
    
        // Collects all the checked checkboxs in the filter-panel
        const checkedBoxes = filterPanel.querySelectorAll('input[type="checkbox"]:checked');
        // Creates a new empty URLSearchParam Object
        const params = new URLSearchParams();

        // Preserves product_types from the current URL and adds them to the start of the query before adding checkbox values
        const currentParams = new URLSearchParams(window.location.search);
        if (currentParams.has('product_types')) {
            params.append('product_types', currentParams.get('product_types'));
        }

        // Preserve the search term from the current URL
        if (currentParams.has('q')) {
            params.append('q', currentParams.get('q'));
        }
    
        // For each checked box append the inputs name and value to params
        checkedBoxes.forEach(function(checkbox) {
            params.append(checkbox.name, checkbox.value);
        });
        
        // Set the URL to specification. Using '.search' only changes the query seciton of the url. Changes made to the URL are automatically executed.
        window.location.search = params.toString();
    });
});