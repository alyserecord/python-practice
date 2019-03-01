def decrypt(encrypted_text, n):
    string = encrypted_text
    for i in range(n):
        string = decryptText(string)
    return string

def decryptText(text):
    t = ''
    b = 0
    mid = int(len(text)/2)
    for i in range(mid):
        t += text[mid + b]
        t += text[b]
        b += 1
    # if len(text) % 2 == 0:
    #     t += text[-2::-2]
    #     t += text[-1::-2]
    # else:    
    #     t += text[-3::-2]
    #     t += text[-2::-2]
    #     t += text[-1]
    return t + text[-1]

def encrypt(text, n):
    string = text
    for i in range(n):
        string = encryptText(string)

    return string

def encryptText(text):
    string = ""

    # Take every 2nd char from the string
    string += text[1::2]
    # Take every not second char
    string += text[::2]
    return string


# Test.describe('Basic Tests')
# Test.assert_equals(encrypt("This is a test!", 0), "This is a test!")
# Test.assert_equals(encrypt("This is a test!", 1), "hsi  etTi sats!")
# Test.assert_equals(encrypt("This is a test!", 2), "s eT ashi tist!")
# Test.assert_equals(encrypt("This is a test!", 3), " Tah itse sits!")
# Test.assert_equals(encrypt("This is a test!", 4), "This is a test!")
# Test.assert_equals(encrypt("This is a test!", -1), "This is a test!")
# Test.assert_equals(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

# Test.assert_equals(decrypt("This is a test!", 0), "This is a test!")
# Test.assert_equals(decrypt("hsi  etTi sats!", 1), "This is a test!")
# Test.assert_equals(decrypt("s eT ashi tist!", 2), "This is a test!")
# Test.assert_equals(decrypt(" Tah itse sits!", 3), "This is a test!")
# Test.assert_equals(decrypt("This is a test!", 4), "This is a test!")
# Test.assert_equals(decrypt("This is a test!", -1), "This is a test!")
# Test.assert_equals(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

# Test.assert_equals(encrypt("", 0), "")
# Test.assert_equals(decrypt("", 0), "")
# Test.assert_equals(encrypt(None, 0), None)
# Test.assert_equals(decrypt(None, 0), None)
