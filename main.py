import os  
import hashlib
from urllib.request import urlretrieve

def checkPath(pathName):
    if pathName not in os.listdir():
        os.mkdir(pathName)
        return 0
    else:
        return 1

def downloadOne(id):
    IMAGE_URL = "https://face-reg.ecnu.edu.cn/image/{0}/{1}.jpg".format(id//100,hashlib.md5(str(id).encode('utf-8')).hexdigest())
    urlretrieve(IMAGE_URL, './{0}/{1}.jpg'.format(id//100,id)) 

def main():
    idPre=101801702
    checkPath(str(idPre))
    for i in range(1,100):
        downloadOne(idPre*100+i)
    return 
    
if __name__=='__main__':
    main()
