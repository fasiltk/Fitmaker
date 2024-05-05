document.addEventListener('DOMContentLoaded', function () {
    const passwordInput = document.getElementById('new_password');
    const confirmPasswordInput = document.getElementById('confirmPassword');
    const registerForm = document.getElementById('registerForm');

    confirmPasswordInput.addEventListener('input', function () {
        if (confirmPasswordInput.value !== passwordInput.value || confirmPasswordInput.value.length < 8) {
            confirmPasswordInput.setCustomValidity('Passwords do not match or are less than 8 characters');
        } else {
            confirmPasswordInput.setCustomValidity(''); // Reset custom validity
        }
    });

    registerForm.addEventListener('submit', function () {
        if (confirmPasswordInput.value !== passwordInput.value || confirmPasswordInput.value.length < 8) {
            confirmPasswordInput.setCustomValidity('Passwords do not match or are less than 8 characters');
        } else {
            confirmPasswordInput.setCustomValidity(''); // Reset custom validity
        }
    });
});
