# Zemerelin Iris M. Membrere
# BSCPE 1-4
# Assignment 2

# Problem 3 - The Vigenere Cipher

# Define function to generate keyword
def Keyword(message, key):
    key = list(key)
# If the length of the message == key, return key
    if len(message) == len(key):
        return key
# If not, append the key
    else:
        for i in range (len(message) - len(key)):
            key.append(key[i % len(key)])
        return ("".join(key))

# Define function to encrypt the message
def encryption(message, key):
    encrypt_message = []
# Add modulo 26 to the message and key
    for i in range(len(message)):
        x = (ord(message[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypt_message.append(chr(x))
    return ("".join(encrypt_message))

if __name__ == "__main__":
# Ask user for the message and keyword all in uppercase letters and no spaces
    message = input("\033[31m\033[1mEnter the message in capital letters and no spaces: \033[35m\033[0m")
    message_keyword = input("\033[31m\033[1mEnter the keyword in capital letters: \033[35m\033[0m")
    key = Keyword(message, message_keyword)
    encrypt_message = encryption(message, key)
# Print the encrypted ciphertext using the Vigenere cipher
    print ("\033[34m\033[1mEncrypted message: \033[35m\033[0m",encrypt_message)