# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import binascii
import random

from ex1 import original1, my_xor, original2, repeated_xor, break_vigenere


def encrypt(text, key):
    # key = random.randint(0, 255).to_bytes(1, byteorder='big')
    res = my_xor(text, (key * len(text)))
    #print(res)
    return (res)

def test_original1():
    key = b'L'
    text = ""
    for i in range(0, 40):
        text+= random.randint(97, 122).to_bytes(1, byteorder='big').decode("ascii")
    #text.__str__().encode()
    print("plaintext: ")
    print(text.encode("ascii"))
    encrypted = encrypt(text.encode("ascii"), key)
    print("input:")
    print(encrypted)
    print("output: ")
    print(original1(encrypted))


def test_original2():
    key = b'L'
    text = ""
    for i in range(0, 40):
        text+= random.randint(48, 57).to_bytes(1, byteorder='big').decode("ascii")
    for i in range(0, 40):
        text+= random.randint(65, 90).to_bytes(1, byteorder='big').decode("ascii")
    for i in range(0, 20):
        text += random.randint(97, 122).to_bytes(1, byteorder='big').decode("ascii")

    #text.__str__().encode()
    print("plaintext: ")
    print(text.encode("ascii"))
    encrypted = encrypt(text.encode("ascii"), key)
    print("input:")
    print(encrypted)
    print("output: ")
    print(original2(encrypted))


def test_repeated_xor():
    print(repeated_xor(b"thebaldeagle", b"LMN"))
# Press the green button in the gutter to run the script.

def hello():
    print("hello")
    
if __name__ == '__main__':
    # print(original1(b"\x38\x24\x29\x2e\x2d\x20\x28\x29\x2d\x2b\x20\x29"))

    test_string = b"thisisatestforyourcode"
    vigenere_key = b"key"
    input_file = b"ciphertext.bin"
    output_file = b"plaintext.txt"
    with open(input_file, "wb") as f:
        f.write(repeated_xor(test_string, vigenere_key))
    key_len = break_vigenere(input_file, output_file)
    assert len(vigenere_key) == key_len
    with open(output_file, "rb") as f:
        result = f.read()
    assert result == test_string
