'''usrinput = input("Hello Skye. Would you like to encrypt or decrypt your files today?\n\n")
encrypt = 'encrypt'
decrypt = 'decrypt'
if usrinput == encrypt:
    import os
    encCommand = os.system('cd;cd Desktop;cd Unlock\ Me;openssl aes-256-cbc -a -k 4545 -salt -in movie.mov -out scytale.enc;rm movie.mov')
if usrinput == decrypt:
    import os
    dencCommand = os.system('cd;cd Desktop;cd Unlock\ Me;openssl aes-256-cbc -a -d -k 4545 -salt -in scytale.enc -out movie.mov;rm scytale.enc')
if usrinput == encrypt:
    print('Ok. Encrypting your files...\n\n\n\n')
    import time
    time.sleep(3)
    print('All done. Exiting...\n\n\n\n')
    import time
    time.sleep(1)
if usrinput == decrypt:
    print('Ok. Decrypting your files...\n\n\n\n')
    import time
    time.sleep(3)
    print('All done. Exiting...\n\n\n\n')
    import time
    time.sleep(1)
import os
os.system('exit')'''




# Start of updated program

import os
import file_traverse

class ENCfile:
    def __init__(self, subfile):
        self.subfile = subfile
        self.supfile = encFileName

    def idFILE(self):
        fileName = file_traverse.__file__
        print(fileName)

    def fileEncProcess(self, fileName): 
        
        print(fileName)


enc_file = ENCfile(file_traverse.__file__)
enc_file.idFILE()
enc_file.fileEncProcess(file_traverse.__usr_direc__, file_traverse.__file__)

print(file_traverse)
