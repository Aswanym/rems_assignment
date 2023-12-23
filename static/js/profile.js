// Get references to the select field and the input fields
const idTypeSelect = document.getElementById('id_type');
const aadharField = document.getElementById('aadharField');
const voterField = document.getElementById('voterField');

// Function to toggle display based on selected option
function toggleFields() {
    if (idTypeSelect.value === 'AADHAR') {
        aadharField.style.display = 'block';
        voterField.style.display = 'none';
    } else if (idTypeSelect.value === 'VOTER') {
        aadharField.style.display = 'none';
        voterField.style.display = 'block';
    } else {
        aadharField.style.display = 'none';
        voterField.style.display = 'none';
    }
}

// Attach an event listener to the select field to trigger the function on change
idTypeSelect.addEventListener('change', toggleFields);

// Call the function initially to set the initial display based on the default selected option
toggleFields();
