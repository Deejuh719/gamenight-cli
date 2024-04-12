text = 'Tdi iiugk xvgkz jot nmabw orij 13 zmdy zsyg.'
custom_key = 'awesome'

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('\tVigenere Cipher')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def vigenere(message, key, direction):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key, 1)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

#print(f'\nOriginal Text: {text}')
#print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
encryption = encrypt(text, custom_key)
#print(f'\nDecrypted/Encrypted Text: {decryption}\n')
if encryption or decryption:
    print(f'\nOriginal Text: {text}')
    print(f'Key: {custom_key}') 
    if encryption:
        print(f'Decrypted Text: {decryption}')
    else:
        print(f'Encrypted Text: {encryption}')
else:
    print('Something went wrong...\nPlease try again. :(')