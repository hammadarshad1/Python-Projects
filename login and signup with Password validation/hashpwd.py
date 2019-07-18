import hashlib

def hashPwd(pwd):
    return hashlib.sha256(str.encode(pwd)).hexdigest()

def checkPwd(pwd,hash):
    if hashPwd(pwd) == hash:
        return True
    else:
        return False