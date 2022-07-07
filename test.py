def my_xor(lhs: bytes, rhs: bytes) -> bytes:
    raise NotImplementedError()


def repeated_xor(plaintext: bytes, key: bytes) -> bytes:
    raise NotImplementedError()


def original1(encrypted: bytes) -> bytes:
    raise NotImplementedError()


def original2(encrypted: bytes) -> bytes:
    raise NotImplementedError()


def break_vigenere(source_path: str, target_path: str) -> int:
    """
    Returns:
        int: Length of the xor-key chosen
    """
    raise NotImplementedError()


def break_shiftedvigenere(source_path: str, target_path: str) -> int:
    raise NotImplementedError()


def example_for_usage():
    result = my_xor(b"\x01\x02\x03", b"\x30\x20\x10")
    assert result == b"\x31\x22\x13"

    result = repeated_xor(b"\x00\x01\x02\x03\x04", b"\x70\x80")
    assert result == b"\x70\x81\x72\x83\x74"

    # NOTE: These test strings are too short for your
    #   functions to actually succeed in the decryption.
    # They are here only so that you can see the expected input
    key = b"K"
    test1 = "test".decode()
    test2 = "This is a test!".decode()
    assert original1(repeated_xor(test1, key)) == test1
    assert original2(repeated_xor(test2, key)) == test2

    # NOTE: Same as before, your code is not expected to work
    #   on this rather short text.
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

    # Shifted vigenere works just the same as the regular vigenere,
    #   but with the key shifted each round.