alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


### Shifting backwards by theshift number


def decrypt(original_text, shift):
    decrypted_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift
        shifted_position = shifted_position % len(alphabet)
        decrypted_text += alphabet[shifted_position]
    print(decrypted_text)

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:
        if encode_or_decode == 'decode':
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position = shifted_position % len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")



#caesar("abcd", 2, 'encode')

direction = input("Type 'encode' to encrypt or 'decode' to decrypt: \n").lower()
original_text = input("Type your message: \n").lower()
shift = int(input("Type your shift amount: \n"))

caesar(original_text, shift, direction)