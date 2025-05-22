// static/script.js
document.addEventListener('DOMContentLoaded', function() {
    const itemsTextarea = document.getElementById('items-input');
    const itemCountDisplay = document.getElementById('item-count');

    if (itemsTextarea && itemCountDisplay) {
        function updateItemCount() {
            const text = itemsTextarea.value;
            const lines = text.split('\n').filter(line => line.trim() !== '');
            // Count unique items for display, matching backend logic for MIN/MAX validation
            const uniqueLines = new Set(lines.map(line => line.trim()));
            itemCountDisplay.textContent = `Items: ${uniqueLines.size}`;
        }

        itemsTextarea.addEventListener('input', updateItemCount);
        
        // Initialize count on page load if there's existing text (e.g., from error or back navigation)
        updateItemCount();
    }

    // Optional: Add client-side validation for number of items before submission
    const inputForm = document.querySelector('form[action="/"]'); // Assuming the index form posts to root
    if (inputForm && itemsTextarea) {
        inputForm.addEventListener('submit', function(event) {
            const text = itemsTextarea.value;
            const lines = text.split('\n').filter(line => line.trim() !== '');
            const uniqueLines = new Set(lines.map(line => line.trim()));
            const count = uniqueLines.size;
            const minItems = 3; // Should match MIN_ITEMS in app.py
            const maxItems = 15; // Should match MAX_ITEMS in app.py

            if (count < minItems || count > maxItems) {
                // This alert is basic. You might replace it with a more integrated error message.
                alert(`Please enter between ${minItems} and ${maxItems} unique items. You have entered ${count}.`);
                event.preventDefault(); // Stop form submission
            }
        });
    }

    // Smooth scroll to sections if you add internal links, etc.
    // Example:
    // document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    //     anchor.addEventListener('click', function (e) {
    //         e.preventDefault();
    //         document.querySelector(this.getAttribute('href')).scrollIntoView({
    //             behavior: 'smooth'
    //         });
    //     });
    // });

    // No complex JS interactions like dynamic card transitions or Chart.js for this version.
    // The "Add Item" button is currently hidden as the primary input is via textarea.
    // If you wanted line-by-line item adding with JS controls, that would be an enhancement here.
});