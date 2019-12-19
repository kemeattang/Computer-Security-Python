

import  affineCipher, detectEnglish, cryptomath

SILENT_MODE = False

def main():
    
    

    f = open("encryptedmessages.txt","r")

    f1 = f.readlines()
    f2 = open("hackedmessages.txt", "w+")
    i = 0

    for x in f1:

        hackmessage = hackAffine(x)
        

        f2.write(hackmessage)

        i = i +1
    f.close()

    f2.close()

def hackAffine(message):
    print('Hacking...')

    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    # Brute-force by looping through every possible key
    if message is None:

        print("we are done")

    for key in range(len(affineCipher.SYMBOLS) ** 2):
        keyA = affineCipher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCipher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Tried Key %s... (%s)' % (key, decryptedText[:40]))



        if detectEnglish.isEnglish(decryptedText):
            # Check with the user if the decrypted key has been found.
            print()
            print('Possible encryption hack:')
            print('Key: %s' % (key))
            print('Decrypted message: ' + decryptedText[:200])
            print()
            
            """
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
            """
            return decryptedText

    
    
    return message


if __name__ == '__main__':
    main()