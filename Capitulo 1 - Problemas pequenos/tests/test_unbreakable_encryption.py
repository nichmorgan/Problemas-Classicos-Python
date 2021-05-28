from unbreakable_encryption import encrypt, decrypt

original = "One Time Pad!"


def test_encryption():
    key1, key2 = encrypt(original)
    print(key1, key2, key1 ^ key2)
    result = decrypt(key1, key2)
    assert original == result
