# Miriam,Jungreis,316287259
# Python 3.9
import re


def my_xor(lhs, rhs):
    res = ""
    for z, k in zip(lhs, rhs):
        hexz = int(hex(z), 16)
        hexk = int(hex(k), 16)
        res += (chr(hexz ^ hexk))
    print(res.encode())
    return res.encode()





def dec(encrypted, key):
    p = ""
    for c in encrypted:
        dec_char = chr(my_xor(chr(c).encode(), key)[0])
        if re.match(r"[a-z]", dec_char) == None:
            return None
        p += dec_char
    return p



def original1(encrypted):
    key_lower_bound = 65
    key_upper_bound = 122
    for i in range(key_lower_bound, key_upper_bound):
        plaintext = dec(encrypted, chr(i).encode())
        if plaintext != None:
            return plaintext




def dec2(encrypted, key):
    p = ""
    for c in encrypted:
        dec_char = chr(my_xor(chr(c).encode(), key)[0])
        if re.match(r"[a-zA-Z0-9]", dec_char) == None and re.match(r"[,.:!?]", dec_char) == None:
            return None
        p += dec_char
    return p


def original2(encrypted):
    char_encrypted = encrypted
    key_lower_bound = 65
    key_upper_bound = 122

    for i in range(key_lower_bound, key_upper_bound):
        plaintext = dec2(char_encrypted, chr(i).encode())
        if (plaintext != None):
            return plaintext


def repeated_xor(plaintext, key):
    enc = ""
    i = 0
    while i < len(plaintext):
        p = plaintext[i:i + len(key)]
        res = my_xor(p, key)
        enc += str(res.decode())
        i += len(key)
    return bytes(enc.encode())


def evaluate_t(buffer, right_t):
    xors = ""
    i = 0
    j=1
    xor_distribution = []
    while i < len(buffer)-right_t:
        res = repeated_xor(buffer[right_t*j:], buffer[i:i+right_t])
        i+=right_t
        j+=1
        xors+=res.decode()
    sum_squers = 0

    for c in xors:
        if int(c.encode("ascii").hex(), 16)>32:
            sum_squers+=1/len(xors)*(1/len(xors))
        if int(c.encode("ascii").hex(), 16)<31 and int(c.encode("ascii").hex(), 16)>16:
            sum_squers+=(1/len(xors)-(32/(13*13)))*(1/len(xors)-(32/(13*13)))
        else:
            sum_squers+=(1/len(xors)-1/16)*(1/len(xors)-1/16)
    return sum_squers






def decrypt(buffer, t):
    length = len(buffer.decode())
    decrypted = buffer(length = length)
    for j in range(0, t-1):
        encrypted = ""
        i = 0
        while i < len(buffer)-1:
            encrypted += buffer[i].__str__()
            i+=t
        print(encrypted)
        dec = original1(encrypted.encode())
        index = 0
        for c in dec:
            decrypted[index]=c.encode()
            index+=t
    return decrypted





def break_vigenere(source_path, target_path):
    input_file = open(source_path, "rb")
    buffer = input_file.read()
    right_t = 1
    t_evaluation = evaluate_t(buffer, right_t)
    for t in range(2, len(buffer)-1):
        res = evaluate_t(buffer, t)
        if(res<t_evaluation):
            right_t = t
            t_evaluation = res
    output_file = open(target_path, "w")
    decryption = decrypt(buffer, t)
    output_file.write(decryption)
    input_file.close()
    output_file.close()
    return t



