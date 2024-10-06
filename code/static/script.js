
function processMessage() {
    // Reset the previous output
    document.getElementById("encryption-status").textContent = "";
    document.getElementById("decrypted-message").textContent = "";
    document.getElementById("signature-status").textContent = "";
    document.getElementById("checkmark").textContent = "";
    
    // Hide previous outputs
    document.getElementById("encryption-status").classList.add("hidden");
    document.getElementById("decrypted-message").classList.add("hidden");
    document.getElementById("signature-status").classList.add("hidden");
    document.getElementById("checkmark").classList.add("hidden");

    const message = document.getElementById("message").value;
    const progressBar = document.getElementById("progress-bar");

    // Show progress bar
    let width = 0;
    const interval = setInterval(() => {
        if (width >= 100) {
            clearInterval(interval);
            showEncryptionSuccess();  // Show encryption success after the bar completes
        } else {
            width += 1;
            progressBar.style.width = width + '%';
        }
    }, 20);

    // Send the message to the Flask app via an AJAX POST request
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/process_message", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            
            // First, show the encryption success message
            setTimeout(() => {
                document.getElementById("encryption-status").textContent = response.encryption_status;
                document.getElementById("encryption-status").classList.remove("hidden");

                // Then show the decrypted message after a slight delay
                setTimeout(() => {
                    document.getElementById("decrypted-message").textContent = response.decrypted_message || 'Decryption failed';
                    document.getElementById("decrypted-message").classList.remove("hidden");

                    // Finally, show the signature validation result and checkmark
                    setTimeout(() => {
                        document.getElementById("signature-status").textContent = response.signature_status;
                        document.getElementById("signature-status").classList.remove("hidden");
                        document.getElementById("checkmark").textContent = response.signature_valid ? '✔' : '✘';
                        document.getElementById("checkmark").classList.remove("hidden");

                        // Reset the progress bar once everything is shown
                        progressBar.style.width = '0%';
                    }, 1000);  // Delay for signature validation
                }, 1000);  // Delay for decryption message
            }, 500);  // Delay for encryption success
        }
    };
    xhr.send("message=" + encodeURIComponent(message));
}
