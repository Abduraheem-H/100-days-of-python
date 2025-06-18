from art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
print(logo)
flag = True
while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs

    def caesar(text, shift, direction):
        end_text = ""
        if direction == "encode":
            for letter in text:
                if letter in alphabet:
                    index = (alphabet.index(letter) + shift) % len(alphabet)
                    end_text += alphabet[index]
                else:
                    end_text += letter
            print(end_text)
        else:
            rev_shift = shift * -1
            for letter in text:
                if letter in alphabet:
                    index = (alphabet.index(letter) + rev_shift) % len(alphabet)
                    end_text += alphabet[index]
                else:
                    end_text += letter
            print(end_text)

    caesar(text, shift, direction)
    key = input(
        "Do you want to encode/decode other text? press any key except N \n"
    ).lower()
    if key == "n":
        flag = False
