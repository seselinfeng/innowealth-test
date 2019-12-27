from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5  # 用于加密
import base64
import Crypto.Signature.PKCS1_v1_5 as sign_PKCS1_v1_5  # 用于签名/验签
from Crypto import Hash
import os

cur_path = os.path.dirname(os.path.realpath(__file__))
key_path = os.path.join(os.path.dirname(cur_path), "data")
if not os.path.exists(key_path):
    os.mkdir(key_path)


def generate_rsa_keys():
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)  # 使用伪随机数来辅助生成
    pubkey = key.publickey().export_key('PEM')  # 默认是 PEM的
    privakey = key.export_key('PEM')

    return pubkey, privakey


def rsaEncrypt(message, pubkey):
    """
    RSA加密
    :param message: 被加密的字符串
    :param pubkey: 公钥
    :return:
    """
    rsakey = RSA.import_key(pubkey)
    cipher = PKCS1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(message.encode()))

    # print(cipher_text)
    return cipher_text


def rsaDecrypt(result, privatekey):
    """
    私钥解密
    :param result:
    :param pubkey:
    :return:
    """
    result = base64.b64decode(result)

    rsakey = RSA.import_key(privatekey)
    cipher = PKCS1_v1_5.new(rsakey)
    content = cipher.decrypt(result, Random.new().read).decode()
    # print(content)


def save(key, filename):
    # 保存密钥
    with open(filename, 'w+') as f:
        f.write(key)


def read(filename):
    # 导入密钥
    with open(filename, 'rb') as f:
        key = f.read()
        return key


def skey_to_pkey(privakey):
    """
    已知私钥的情况下，生成公钥
    :param privakey:
    :return:
    """
    s_key = RSA.import_key(privakey)
    p_key = s_key.publickey().export_key()

    return p_key


def sign_with_privakey(message, private_key=''):
    """
    私钥签名
    :param message:明文
    :param privakey:
    :return:密文
    """
    private_key = read("{}{}".format(key_path, '/private_key.pem'))
    signer = sign_PKCS1_v1_5.new(RSA.import_key(private_key))
    rand_hash = Hash.SHA1.new()
    rand_hash.update(message.encode())
    signature = signer.sign(rand_hash)
    # print(signature.decode('utf-8', 'ignore'))
    return signature


def verify_with_pubkey(signature, message, pubkey):
    """
    公钥验签
    :param signature:密文
    :param message:明文
    :param pubkey:公钥
    :return:
    """
    verifier = sign_PKCS1_v1_5.new(RSA.import_key(pubkey))
    rand_hash = Hash.SHA1.new()
    rand_hash.update(message.encode())
    return verifier.verify(rand_hash, signature)


def execute_without_signature(message,pubkey, privakey):
    """
    公钥加密，私钥解密
    :param pubkey:
    :param privakey:
    :return:
    """
    # message = 'address=n3CucMR3dYZzcFmzU6WSDb9QejBWCUaqPz&memo=123&requestNo=FO20000000000'
    result = rsaEncrypt(message, pubkey)
    rsaDecrypt(result, privakey)
    print("rsa test success！")


def execute_with_signature(text,pubkey, privakey):
    """
    签名验证，不加密
    :param pubkey:
    :param privakey:
    :return:
    """
    # text = 'address=n3CucMR3dYZzcFmzU6WSDb9QejBWCUaqPz&memo=123&requestNo=FO20000000000'
    assert verify_with_pubkey(sign_with_privakey(text, privakey), text, pubkey)
    print("rsa Signature verified!")


def encrypt_and_decrypt_test(password="123456"):
    # 加载私钥用于加密
    recipient_key = read("{}{}".format(key_path, '/private_key.pem'))
    cipher_rsa = PKCS1_v1_5.new(recipient_key)
    # 使用base64编码保存数据方便查看，同样解密需要base64解码
    en_data = base64.b64encode(cipher_rsa.encrypt(b'123456'))
    print("加密数据信息：", type(en_data), '\n', len(en_data), '\n', en_data)

    # 加载公钥用于解密
    encoded_key = read("{}{}".format(key_path, '/public_key.pem'))
    private_key = RSA.import_key(encoded_key, passphrase=password)
    cipher_rsa = PKCS1_v1_5.new(private_key)
    data = cipher_rsa.decrypt(base64.b64decode(en_data), None)
    print(data)



if __name__ == '__main__':
    private_key = read("{}{}".format(key_path, '/private_key.pem'))
    public_key = read("{}{}".format(key_path, '/public_key.pem'))
    # pubkey, privakey = generate_rsa_keys()
    import binascii
    message = 'address=n3CucMR3dYZzcFmzU6WSDb9QejBWCUaqPz&memo=123&requestNo=FO20000000000'
    ############ 使用公钥 - 私钥对信息进行"加密" + "解密" ##############
    execute_without_signature(message,public_key, private_key)
    ############ 使用私钥 - 公钥对信息进行"签名" + "验签" ##############
    execute_with_signature(message,public_key, private_key)
    s = sign_with_privakey(message, private_key)
    print(base64.b64encode(s))
