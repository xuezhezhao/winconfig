import base64
from Crypto.Cipher import PKCS1_v1_5
from Crypto import Random
from Crypto.PublicKey import RSA

#
# def decryption(text_encrypted_base64: str, private_key: bytes):
#     # 字符串指定编码（转为bytes）
#     text_encrypted_base64 = text_encrypted_base64.encode('utf-8')
#     # base64解码
#     text_encrypted = base64.b64decode(text_encrypted_base64)
#     # 构建私钥对象
#     cipher_private = PKCS1_v1_5.new(RSA.importKey(private_key))
#     # 解密（bytes）
#     text_decrypted = cipher_private.decrypt(text_encrypted, Random.new().read)
#     # 解码为字符串
#     text_decrypted = text_decrypted.decode()
#     return text_decrypted
#
#
# if __name__ == '__main__':
#     # # 生成密文
#     # public_key = read_public_key()
#     # text = '123456'
#     # text_encrypted_base64 = encryption(text, public_key)
#     # print('密文：', text_encrypted_base64)
#     #
#     # # 解密
#     # private_key = read_private_key()
#     # text_decrypted = decryption(text_encrypted_base64, private_key)
#     # print('明文：', text_decrypted)
#     PrivateKey="MIICXQIBAAKBgQC7PyjMEuniN6BPn8oqzIZ6AO1NjSTO9R3adCCIwKfKIEoWXXM+tHDpktdPKSaAsWJPTNAGvEvtxOfzXib/EMXKqD0eUy5MatfpRjRdf1hJVimmfrb09Qx2j7CsKLy7nD23m4xubdYBwvkjMwt/L3JxB5D6qryW1wei/j1c+/OCxQIDAQABAoGAT7vGYJgRNf4f6qgNS4pKHTu10RcwPFyOOM7IZ9M5380+HyXuBB6MEjowKwpH1fcy+LepwaR+5KG7b5uBGY4H2ticMtdysBd9gLwnY4Eh4j7LCWE54HvELpeWXkWpFQdb/NQhcqMAGwYsTnRPdBqkrUmJBTYqEGkIlqCQ5vUJOCECQQDhe0KGmbq1RWp6TDvgpA2dUmlt2fdP8oNW8O7MvbDaQRduoZnVRTPYCDKfzFqpNXL1hAYgth1N0vzDnv3VoLcpAkEA1JcY+rLv5js1g5Luv8LaI5/3uOg0CW7fmh/LfGuz8k/OxASN+cAOUjPHrxtc5xn1zat4/bnV5GEdlOp/DhquPQJBAIV2Fsdi4M+AueiPjPWHRQO0jvDVjfwFOFZSn5YSRUa6NmtmPY6tumUJXSWWqKb1GwlVTuc3xBqXYsNLLUWwLhkCQQDJUJCiD0LohhdGEqUuSKnj5H9kxddJO4pZXFSI7UEJbJQDwcBkyn+FTm2BH+tZGZdQfVnlA89OJr0poOpSg+eNAkAKY85SR9KASaTiDBoPpJ8N805XEhd0Kq+ghzSThxL3fVtKUQLiCh7Yd8oMd/G5S3xWJHUXSioATT8uPRH2bOb/"
#     PublicKey="MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC7PyjMEuniN6BPn8oqzIZ6AO1NjSTO9R3adCCIwKfKIEoWXXM+tHDpktdPKSaAsWJPTNAGvEvtxOfzXib/EMXKqD0eUy5MatfpRjRdf1hJVimmfrb09Qx2j7CsKLy7nD23m4xubdYBwvkjMwt/L3JxB5D6qryW1wei/j1c+/OCxQIDAQAB"
#     password='szfOhjNyqDr3S0yhhHie6n7urr8Aa8qPFi9Ju6pHJEm5Pwfk+b8BZEf4K7YtKQRiClLoqC57/qgvdz6ZdQmKPLS9GoiQdzg5XkwuluWYMFk5UdqMlr6HgD1ztDHdYwzfd+r9ECKUpAFEFaJZMWwkT/p3XoN6pfPA5MzVJGeRgo0='
#     print('明文：',decryption(password,PrivateKey))


import base64
import rsa
from datetime import datetime
from Crypto.PublicKey import RSA

# Master使用Ghost的公钥对内容进行rsa 加密


from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5


PrivateKey="MIICXQIBAAKBgQC7PyjMEuniN6BPn8oqzIZ6AO1NjSTO9R3adCCIwKfKIEoWXXM+tHDpktdPKSaAsWJPTNAGvEvtxOfzXib/EMXKqD0eUy5MatfpRjRdf1hJVimmfrb09Qx2j7CsKLy7nD23m4xubdYBwvkjMwt/L3JxB5D6qryW1wei/j1c+/OCxQIDAQABAoGAT7vGYJgRNf4f6qgNS4pKHTu10RcwPFyOOM7IZ9M5380+HyXuBB6MEjowKwpH1fcy+LepwaR+5KG7b5uBGY4H2ticMtdysBd9gLwnY4Eh4j7LCWE54HvELpeWXkWpFQdb/NQhcqMAGwYsTnRPdBqkrUmJBTYqEGkIlqCQ5vUJOCECQQDhe0KGmbq1RWp6TDvgpA2dUmlt2fdP8oNW8O7MvbDaQRduoZnVRTPYCDKfzFqpNXL1hAYgth1N0vzDnv3VoLcpAkEA1JcY+rLv5js1g5Luv8LaI5/3uOg0CW7fmh/LfGuz8k/OxASN+cAOUjPHrxtc5xn1zat4/bnV5GEdlOp/DhquPQJBAIV2Fsdi4M+AueiPjPWHRQO0jvDVjfwFOFZSn5YSRUa6NmtmPY6tumUJXSWWqKb1GwlVTuc3xBqXYsNLLUWwLhkCQQDJUJCiD0LohhdGEqUuSKnj5H9kxddJO4pZXFSI7UEJbJQDwcBkyn+FTm2BH+tZGZdQfVnlA89OJr0poOpSg+eNAkAKY85SR9KASaTiDBoPpJ8N805XEhd0Kq+ghzSThxL3fVtKUQLiCh7Yd8oMd/G5S3xWJHUXSioATT8uPRH2bOb/"
PublicKey="MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC7PyjMEuniN6BPn8oqzIZ6AO1NjSTO9R3adCCIwKfKIEoWXXM+tHDpktdPKSaAsWJPTNAGvEvtxOfzXib/EMXKqD0eUy5MatfpRjRdf1hJVimmfrb09Qx2j7CsKLy7nD23m4xubdYBwvkjMwt/L3JxB5D6qryW1wei/j1c+/OCxQIDAQAB"
password='szfOhjNyqDr3S0yhhHie6n7urr8Aa8qPFi9Ju6pHJEm5Pwfk+b8BZEf4K7YtKQRiClLoqC57/qgvdz6ZdQmKPLS9GoiQdzg5XkwuluWYMFk5UdqMlr6HgD1ztDHdYwzfd+r9ECKUpAFEFaJZMWwkT/p3XoN6pfPA5MzVJGeRgo0='

start = '-----BEGIN PUBLIC KEY-----\n'
end = '-----END PUBLIC KEY-----'
result = ''
# 分割key，每64位长度换一行
divide = int(len(PublicKey) / 64)
divide = divide if (divide > 0) else divide + 1
line = divide if (len(PublicKey) % 64 == 0) else divide + 1
for i in range(line):
    result += PublicKey[i * 64:(i + 1) * 64] + '\n'
result = start + result + end
print(result)

rsakey = RSA.importKey(result)
cipher=Cipher_pkcs1_v1_5.new(rsakey)
# message='Winner@001'
cipher_text=base64.b64encode(cipher.encrypt('Winner@001'))
print(cipher_text)
