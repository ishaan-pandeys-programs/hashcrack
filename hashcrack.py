from urllib.request import urlopen, hashlib
import time

gibberishtype = input('Enter the type of hash here (HashCrack can only decrypt SHA and MD5 hashes, and please type the hash type only in lowercase): ')

if gibberishtype.find('s') == 0:
    specificgibberishtype = input('Enter the specific type of SHA hash (type only the number, for example if you want sha256 just type 256, or for sha1, just type 1. But if you want to crack sha224, then type 024 and not 224): ')
    if specificgibberishtype.find('5') == 1:
        sha256hash = input("Please input the sh256 hash to crack.\n>")
        LIST_OF_WORDS = str(urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt').read(), 'utf-8')
        for guess in LIST_OF_WORDS.split('\n'):
            hashedGuess = hashlib.sha3_256(bytes(guess, 'utf-8')).hexdigest()
            if hashedGuess == sha256hash:
                print("The hash plaintext is ", str(guess))
                time.sleep(5)
                quit()
            
        print("Hash plaintext not in database, we'll get them next time. Unless you want to try a dictionary attack with a txt file on the same hash?")
        task = input("Type yes or no to dictionary attack with txt file: ")
        if task.find('y') >= 0:
            dictionary = input('Enter dictionary filepath: ')

            try:
                pass_file = open(dictionary, "r")
            except:
                print('No file found or wrong type of file. Program terminating...')
                time.sleep(5)
                quit()
            for word in pass_file:
                encode = word.encode('utf-8')
                digest = hashlib.sha3_256(encode.strip()).hexdigest()

                if digest == sha256hash:
                    print('Hash plaintext found. Dictionary attack with txt file succesful.')
                    print('The plaintext is: ' + word)
                    time.sleep(5)
                    quit()
            print('Hash plaintext does nor appear to be in the dictionary file. Password crack failed. Program terminating...')
            time.sleep(5)
            quit()
        else:
            print('Well, that\'s it, then. Decryption failed. Program terminating...')
            time.sleep(5)
            quit()
    elif specificgibberishtype.find('1') == 0:
        sha1hash = input("Please input the sha1 hash to crack.\n>")
        LIST_OF_WORDS = str(urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt').read(), 'utf-8')
        for guess in LIST_OF_WORDS.split('\n'):
            hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
            if hashedGuess == sha1hash:
                print("The hash plaintext is ", str(guess))
                time.sleep(5)
                quit()
        print("Hash plaintext not in database, we'll get them next time. Unless you want to try a dictionary attack with a txt file on the same hash?")
        task = input("Type yes or no to dictionary attack with txt file: ")
        if task.find('y') >= 0:
            dictionary = input('Enter dictionary filepath: ')

            try:
                pass_file = open(dictionary, "r")
            except:
                print('No file found or wrong type of file. Program terminating...')
                time.sleep(5)
                quit()
            for word in pass_file:
                encode = word.encode('utf-8')
                digest = hashlib.sha1(encode.strip()).hexdigest()

                if digest == sha1hash:
                    print('Hash plaintext found. Dictionary attack with txt file succesful.')
                    print('The plaintext is: ' + word)
                    time.sleep(5)
                    quit()
            print('The hash plaintext does nor appear to be in the dictionary file. Password crack failed. Program terminating...')
            time.sleep(5)
            quit()
        else:
            print('Well, that\'s it, then. Decryption failed. Program terminating...')
            time.sleep(5)
            quit()
    elif specificgibberishtype.find('2') == 1:
        sha224hash = input("Please input the sha224 hash to crack.\n>")
        LIST_OF_WORDS = str(urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt').read(), 'utf-8')
        for guess in LIST_OF_WORDS.split('\n'):
            hashedGuess = hashlib.sha3_224(bytes(guess, 'utf-8')).hexdigest()
            if hashedGuess == sha224hash:
                print("The hash plaintext is ", str(guess))
                time.sleep(5)
                quit()
           
        print("Hash plaintext not in database, we'll get them next time. Unless you want to try a dictionary attack with a txt file on the same hash?")
        task = input("Type yes or no to dictionary attack with txt file: ")
        if task.find('y') >= 0:
            dictionary = input('Enter dictionary filepath: ')

            try:
                pass_file = open(dictionary, "r")
            except:
                print('No file found or wrong type of file. Program terminating...')
                time.sleep(5)
                quit()
            for word in pass_file:
                encode = word.encode('utf-8')
                digest = hashlib.sha3_224(encode.strip()).hexdigest()

                if digest == sha224hash:
                    print('Hash plaintext found. Dictionary attack with txt file succesful.')
                    print('The plaintext is: ' + word)
                    time.sleep(5)
                    quit()
            print('The hash plaintext does nor appear to be in the dictionary file. Password crack failed. Program terminating...')
            time.sleep(5)
            quit()
        else:
            print('Well, that\'s it, then. Decryption failed. Program terminating...')
            time.sleep(5)
            quit()
    elif specificgibberishtype.find('3') == 0:

        sha384hash = input("Please input the sha384 hash to crack.\n>")
        LIST_OF_WORDS = str(urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt').read(), 'utf-8')
        for guess in LIST_OF_WORDS.split('\n'):
            hashedGuess = hashlib.sha3_384(bytes(guess, 'utf-8')).hexdigest()
            if hashedGuess == sha384hash:
                print("The plaintext for the hash is ", str(guess))
                time.sleep(5)
                quit()
           
        print("Hash plaintext not in database, we'll get them next time. Unless you want to try a dictionary attack with a txt file on the same hash?")
        task = input("Type yes or no to dictionary attack with txt file: ")
        if task.find('y') >= 0:
            dictionary = input('Enter dictionary filepath: ')

            try:
                pass_file = open(dictionary, "r")
            except:
                print('No file found or wrong type of file. Program terminating...')
                time.sleep(5)
                quit()
            for word in pass_file:
                encode = word.encode('utf-8')
                digest = hashlib.sha3_384(encode.strip()).hexdigest()

                if digest == sha384hash:
                    print('Hash plaintext found. Dictionary attack with txt file succesful.')
                    print('The plaintext for the hash is: ' + word)
                    time.sleep(5)
                    quit()
            print('The hash  does nor appear to be in the dictionary file. Password crack failed. Program terminating...')
            time.sleep(5)
            quit()
        else:
            print('Well, that\'s it, then. Decryption failed. Program terminating...')
            time.sleep(5)
            quit()
    elif specificgibberishtype.find('5') == 0:
        sha512hash = input("Please input the sha512 hash to crack.\n>")
        LIST_OF_WORDS = str(urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt').read(), 'utf-8')
        for guess in LIST_OF_WORDS.split('\n'):
            hashedGuess = hashlib.sha3_512(bytes(guess, 'utf-8')).hexdigest()
            if hashedGuess == sha512hash:
                print("The plaintext for the hash is ", str(guess))
                time.sleep(5)
                quit()
            
        print("Hash plaintext not in database, we'll get them next time. Unless you want to try a dictionary attack with a txt file on the same hash?")
        task = input("Type yes or no to dictionary attack with txt file: ")
        if task.find('y') >= 0:
            dictionary = input('Enter dictionary filepath: ')

            try:
                pass_file = open(dictionary, "r")
            except:
                print('No file found or wrong type of file. Program terminating...')
                time.sleep(5)
                quit()
            for word in pass_file:
                encode = word.encode('utf-8')
                digest = hashlib.sha3_512(encode.strip()).hexdigest()

                if digest == sha512hash:
                    print('Hash cracked successfully. Dictionary attack with txt file succesful.')
                    print('The plaintext for the hash is: ' + word)
                    time.sleep(5)
                    quit()
            print('The hash plaintext does nor appear to be in the dictionary file. Password crack failed. Program terminating...')
            time.sleep(5)
            quit()
        else:
            print('Well, that\'s it, then. Decryption failed. Program terminating...')
            time.sleep(5)
            quit()
    else:
        print('Hash type not supported. HashCrack is terminating..')
        time.sleep(5)
        quit()
elif gibberishtype.find('m') == 0:
    md5hash = input("Please input the md5 hash to crack.\n>")
    LIST_OF_WORDS = str(urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt').read(), 'utf-8')
    for guess in LIST_OF_WORDS.split('\n'):
        hashedGuess = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == md5hash:
            print("The plaintext for the hash is ", str(guess))
            time.sleep(5)
            quit()
       
    print("Hash plaintext in database, we'll get them next time. Unless you want to try a dictionary attack with a txt file on the same hash?")
    task = input("Type yes or no to dictionary attack with txt file: ")
    if task.find('y') >= 0:
        dictionary = input('Enter dictionary filepath: ')

        try:
            pass_file = open(dictionary, "r")
        except:
            print('No file found or wrong type of file. Program terminating...')
            time.sleep(5)
            quit()
        for word in pass_file:
            encode = word.encode('utf-8')
            digest = hashlib.md5(encode.strip()).hexdigest()

            if digest == md5hash:
                print('Hash plaintext found. Dictionary attack with txt file succesful.')
                print('The plaintext is: ' + word)
                time.sleep(5)
                quit()
        print('The hash plaintext does nor appear to be in the dictionary file. Password crack failed. Program terminating...')
        time.sleep(5)
        quit()
    else:
        print('Well, that\'s it, then. Decryption failed. Program terminating...')
        time.sleep(5)
        quit()
else:
    print('Hash type not supported. HashCrack is terminating...')
    time.sleep(5)
    quit()
