import rsa

# Generate public and private keys
(public_key, private_key) = rsa.newkeys(1024)  # Note: For real applications, use at least 2048 bits for security.

def encrypt_message(message, pub_key):
    encrypted_bytes = rsa.encrypt(message.encode(), pub_key)
    encrypted_number = int.from_bytes(encrypted_bytes, 'big')
    return encrypted_number

def decrypt_message(encrypted_number, priv_key):
    encrypted_bytes = encrypted_number.to_bytes((encrypted_number.bit_length() + 7) // 8, 'big')
    return rsa.decrypt(encrypted_bytes, priv_key).decode()


def test_rsa(messages):
    for message in messages:
        print(f"\nTesting message: '{message}'")
        try:
            encrypted_number = encrypt_message(message, public_key)
            decrypted_message = decrypt_message(encrypted_number, private_key)
            print("Original:", message)
            print("Encrypted:", encrypted_number)
            print("Decrypted:", decrypted_message)
            assert message == decrypted_message, "Decryption does not match original!"
        except AssertionError as e:
            print("Test result: Failed -", e)
        except Exception as e:
            print("Test result: Failed with error:", str(e))

# List of sample messages to test
test_messages = [
    "Hello World!",
    " +-@#}{()][", # Special characters
    "A very long message " * 10,  # Long message
    "1234567890", # Number
    "She sells seashells by the seashore"
]

# Execute the tests
test_rsa(test_messages)