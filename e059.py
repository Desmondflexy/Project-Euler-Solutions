def decrypt_with_key(ciphertext, key):
    key_length = len(key)
    decrypted = []
    for i, byte in enumerate(ciphertext):
        decrypted_byte = byte ^ key[i % key_length]
        decrypted.append(decrypted_byte)
    return decrypted


def is_english_word(word, word_list):
    return word.lower() in word_list


def find_sum_of_ascii_values(decrypted_text):
    return sum(decrypted_text)


# Step 1: Read the encrypted ASCII codes from the file
with open('p059_cipher.txt', 'r') as file:
    encrypted_text = file.read().strip().split(',')

encrypted_text = list(map(int, encrypted_text))
# print(encrypted_text)

# Step 2: Load the word list or dictionary for English words
# You can replace 'word_list.txt' with the path to your word list file
with open('word_list.txt', 'r') as file:
    word_list = [word.strip().lower() for word in file.readlines()]
    print(word_list)

# Step 3: Brute-force approach to find the correct key
possible_keys = [chr(a) + chr(b) + chr(c) for a in range(97, 123)
                 for b in range(97, 123) for c in range(97, 123)]

for key in possible_keys:
    decrypted_text = decrypt_with_key(encrypted_text, [ord(char) for char in key])
    decrypted_text = ''.join(chr(byte) for byte in decrypted_text)

    # Step 7: Check if the decrypted text contains common English words
    if is_english_word(decrypted_text, word_list):
        # Step 9: Calculate the sum of the ASCII values
        sum_ascii_values = find_sum_of_ascii_values(decrypted_text)
        print("Decrypted text:")
        print(decrypted_text)
        print("Sum of ASCII values in the original text:")
        print(sum_ascii_values)
        break


# incorrect