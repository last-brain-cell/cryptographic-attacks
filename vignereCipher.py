def generate_key(text, key):
    key = list(key)
    if len(key) >= len(text):
        return ''.join(key[:len(text)])
    else:
        return ''.join(key[i % len(key)] for i in range(len(text)))

def encrypt_vigenere(text, key):
    encrypted_text = []
    key = generate_key(text, key)
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i].upper()) - ord('A')
            if text[i].isupper():
                encrypted_text.append(chr((ord(text[i]) - ord('A') + shift) % 26 + ord('A')))
            else:
                encrypted_text.append(chr((ord(text[i]) - ord('a') + shift) % 26 + ord('a')))
        else:
            encrypted_text.append(text[i])
    return ''.join(encrypted_text)

def decrypt_vigenere(text, key):
    decrypted_text = []
    key = generate_key(text, key)
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i].upper()) - ord('A')
            if text[i].isupper():
                decrypted_text.append(chr((ord(text[i]) - ord('A') - shift) % 26 + ord('A')))
            else:
                decrypted_text.append(chr((ord(text[i]) - ord('a') - shift) % 26 + ord('a')))
        else:
            decrypted_text.append(text[i])
    return ''.join(decrypted_text)


plaintext = input("enter the text: ")
key = "uday dasari"
ciphertext = encrypt_vigenere(plaintext, key)
decrypted_text = decrypt_vigenere(ciphertext, key)

print("Encrypted:", ciphertext)
print("Decrypted:", decrypted_text)
