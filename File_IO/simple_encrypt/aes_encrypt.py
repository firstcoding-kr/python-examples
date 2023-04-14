from cryptography.fernet import Fernet
# 설치: pip install cryptography

# 암호화 키 생성
key = Fernet.generate_key()

# Fernet 객체 생성
fernet = Fernet(key)

# 암호화 함수
def encrypt(text):
    encrypted_text = fernet.encrypt(text.encode('utf-8'))
    return encrypted_text.decode('utf-8')

# 복호화 함수
def decrypt(encrypted_text):
    decrypted_text = fernet.decrypt(encrypted_text.encode('utf-8'))
    return decrypted_text.decode('utf-8')

# 텍스트 암호화
text = '암호화할 텍스트'
encrypted_text = encrypt(text)
print('암호화된 텍스트:', encrypted_text)

# 텍스트 복호화
decrypted_text = decrypt(encrypted_text)
print('복호화된 텍스트:', decrypted_text)
