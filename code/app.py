from flask import Flask, render_template, request, jsonify
import time
import numpy as np
from encryption import encrypt_message, decrypt_message
from signing import sign_message, verify_signature
from ml_model import train_model, predict_security_risk
from utils import generate_rsa_key_pair

app = Flask(__name__)

# Step 1: Generate RSA key pairs at the start
private_key_decryption, public_key_encryption = generate_rsa_key_pair()  # Recipient's keys
private_key_signing, public_key_verification = generate_rsa_key_pair()  # Sender's keys

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_message', methods=['POST'])
def process_message():
    # Step 2: Receive the message from the form
    message = request.form['message'].encode()

    # Step 3: Encrypt the message using the recipient's public key
    start_encrypt_time = time.time()
    encrypted_message = encrypt_message(message, public_key_encryption)
    end_encrypt_time = time.time()
    encryption_time = end_encrypt_time - start_encrypt_time

    # Step 4: Sign the original message using the sender's private key
    signature = sign_message(message, private_key_signing)

    # Step 5: Feature extraction for ML model (assuming no risk example)
    message_length = len(message)
    encrypted_message_length = len(encrypted_message)
    message_entropy = 0.9  # Placeholder
    network_activity = 120  # Simulated metric
    features = np.array([[message_length, encrypted_message_length, message_entropy, encryption_time, network_activity]])


    # Step 5: Feature extraction for the ML model (SHOWING RISK)
    # message_length = len(message)  # Length of the input message
    # encrypted_message_length = len(encrypted_message) + 100  # Simulate a longer encrypted message
    # message_entropy = 0.4  # Lower entropy indicates less randomness (riskier)
    # encryption_time = 0.05  # Longer encryption time can indicate problems    
    # network_activity = 300  # Simulated high network activity
    # features = np.array([[message_length, encrypted_message_length, message_entropy, encryption_time, network_activity]])


    # Step 6: Load and train the classifier
    classifier = train_model()

    # Step 7: Use ML model to predict security
    prediction = predict_security_risk(features, classifier)

    if prediction == 1:
        signature_valid = verify_signature(message, signature, public_key_verification)
        if signature_valid:
            decrypted_message = decrypt_message(encrypted_message, private_key_decryption)
            response = {
                'encryption_status': "Encryption successful!",
                'decrypted_message': decrypted_message.decode(),
                'signature_valid': True,
                'signature_status': "Signature successfully validated!",
                'prediction': "safe"
            }
        else:
            response = {
                'encryption_status': "Encryption successful!",
                'decrypted_message': None,
                'signature_valid': False,
                'signature_status': "Signature validation failed!",
                'prediction': "safe"
            }
    else:
        response = {
            'encryption_status': "Encryption successful!",
            'decrypted_message': None,
            'signature_valid': False,
            'signature_status': "Signature validation failed!",
            'prediction': "risky"
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
