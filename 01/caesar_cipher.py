import string


def shift_letter(char, key):
    if char.isalpha():
        alphabet = string.ascii_uppercase if char.isupper() else string.ascii_lowercase
        index = alphabet.index(char)
        shifted_index = (index + key) % 26
        return alphabet[shifted_index]
    return char


def encrypt_message(message, key):
    encrypted_message = ''.join(shift_letter(char, key) for char in message)
    encrypted_message = encrypted_message.upper()
    return encrypted_message


def decrypt_message(message, key):
    encrypted_message = encrypt_message(message, -key)
    return encrypted_message.upper()


while True:
    choice = input('Do you want to (e)ncrypt or (d)ecrypt?\n').lower()
    if choice not in ("e", "d"):
        print('Please enter "e" for encrypt or "d" for decrypt')
        continue
    try:
        key = int(input('Please enter the key (0 to 25) to use.\n'))
        if not 0 <= key <= 25:
            print('Please enter a valid key in the range 0 to 25.')
            continue
        result = ''
        if choice == "e":
            message = input('Enter the message to encrypt.\n')
            result = encrypt_message(message, key)
        elif choice == "d":
            message = input('Enter the message to decrypt.\n')
            result = decrypt_message(message, key)
        print(result)

    except ValueError:
        print('Invalid input. Please enter numeric key.')
