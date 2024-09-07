import zipfile

def crack_zip(zip_file, password_list):
    with zipfile.ZipFile(zip_file, 'r') as zfile:
        with open(password_list, 'r') as passwords:
            for password in passwords:
                password = password.strip()
                try:
                    zfile.extractall(pwd=password.encode('utf-8'))
                    print(f"Password found: {password}")
                    return True
                except (RuntimeError, zipfile.BadZipFile):
                    # Incorrect password or bad zip file
                    continue
    print("Password not found.")
    return False

# Usage example:
zip_file = 'protected.zip'  # Path to your zip file
password_list = 'passwords.txt'  # Path to your password dictionary file
crack_zip(zip_file, password_list)
