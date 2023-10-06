from cryptography.fernet import Fernet
import os

def generate_key():
    # Generate a random encryption key
    key = Fernet.generate_key()
    return key

def encrypt_data(data, key):
    # Create a Fernet cipher using the key
    cipher_suite = Fernet(key)

    # Encrypt the sensitive information
    encrypted_info = cipher_suite.encrypt(data.encode())
    return encrypted_info

def decrypt_data(encrypted_data, key):
    # Create a Fernet cipher using the key
    cipher_suite = Fernet(key)

    # Decrypt the encrypted data
    decrypted_info = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_info

def main():
    print("Encryption and Decryption Script")

    # Generate or load encryption key
    if os.path.exists("encryption_key.txt"):
        with open("encryption_key.txt", "rb") as key_file:
            key = key_file.read()
    else:
        key = generate_key()
        with open("encryption_key.txt", "wb") as key_file:
            key_file.write(key)

    choice = input("Choose an option (E)ncrypt or (D)ecrypt: ").strip().lower()

    if choice == "e":
        sensitive_info = input("Enter the sensitive information to encrypt: ")
        file_name = input("Enter the name for the encrypted file (without extension): ")

        # Encrypt the data
        encrypted_info = encrypt_data(sensitive_info, key)

        # Save the encrypted data to a file
        with open(f"{file_name}.txt", "wb") as file:
            file.write(encrypted_info)

        print(f"Encrypted data saved as '{file_name}.txt'")

    elif choice == "d":
        file_name = input("Enter the name of the encrypted file (without extension): ")

        # Read the encrypted data from the file
        with open(f"{file_name}.txt", "rb") as file:
            encrypted_data = file.read()

        try:
            # Decrypt the data
            decrypted_info = decrypt_data(encrypted_data, key)
            print("Decrypted Info:", decrypted_info)

        except Exception as e:
            print("Error:", e)

    else:
        print("Invalid choice. Choose (E)ncrypt or (D)ecrypt.")

if __name__ == "__main__":
    main()
