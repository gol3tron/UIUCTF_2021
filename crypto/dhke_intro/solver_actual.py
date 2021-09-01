import random
from Crypto.Cipher import AES

# generate key
gpList = [ [13, 19], [7, 17], [3, 31], [13, 19], [17, 23], [2, 29] ]

iv = bytes("kono DIO daaaaaa", encoding = 'ascii')
input = b'b31699d587f7daf8f6b23b30cfee0edca5d6a3594cd53e1646b9e72de6fc44fe7ad40f0ea6'
ciphertext = bytearray.fromhex(input.decode())

# trying to guess k to decrypt
for iter in range(len(gpList)):
    # going to brute force try every possible gp combo from given options
    g_try = gpList[iter][0]
    p_try = gpList[iter][1]

    for a_try in range(g_try):
        for b_try in range(p_try):

            # make a new k to try
            k_try = pow(g_try, a_try * b_try, p_try)
            k_try = str(k_try)

            # make a new key w/ padding
            # pad key to 16 bytes (128bit)
            key_try = ""
            i = 0
            padding = "uiuctf2021uiuctf2021"
            while (16 - len(key_try) != len(k_try)):
                key_try = key_try + padding[i]
                i += 1
            key_try = key_try + k_try
            key_try = bytes(key_try, encoding='ascii')

            # attempt decrypt w/ key_try and iv given
            cipher_out = AES.new(key_try, AES.MODE_CFB, iv)
            pt = cipher_out.decrypt(ciphertext)

            # assume the flag starts with uiuctf string
            #if x.decode()[0:6] == 'uiuctf':
            #print("a_try was "+str(a_try))
            #print("b_try was "+str(b_try))
            #print("k_try was "+str(k_try))
            print(pt)
