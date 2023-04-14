pw = 123123
pw = pw % 11 - 27 # 간단한 패스워드 공식

def encrypt(text):
    result = ""
  
    for char in text:
        result += chr(ord(char) + pw)
  
    return result

def decrypt(text):
    result = ""
  
    for char in text:
        result += chr(ord(char) - pw)
  
    return result

# test

source = "Hello 안녕하세요 퍼스트코딩입니다."

# 암호화
encrypted = encrypt(source)
print(encrypted)

# 복호화
decrypted = decrypt(encrypted)
print(decrypted)
