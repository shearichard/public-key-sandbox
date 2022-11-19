import nacl.utils
from nacl.public import PrivateKey, Box
import pprint
import base64

def do_anyone():
    secret_key = PrivateKey.generate()

    if False:
        print(secret_key)
        print(base64.b64encode(secret_key.__bytes__()))
        print(secret_key.SIZE)
        print(secret_key.SEED_SIZE)

    print("")
    public_key = secret_key.public_key
    if False:
        print(public_key)
        pprint.pprint(dir(public_key))
    #
    return {'secretkey': secret_key, 'publickey': public_key}

def main():
    #
    alice_key_dir = do_anyone()
    bob_key_dir= do_anyone()
    #
    pprint.pprint(alice_key_dir)
    pprint.pprint(bob_key_dir)
    #
    bob_box = Box(bob_key_dir['secretkey'], alice_key_dir['publickey'])
    #
    if False:
        pprint.pprint(dir(bob_box))
    #
    message = b"mary had a little lamb"
    #
    encrypted = bob_box.encrypt(message)
    #
    print(encrypted)
    #
    alice_box = Box(alice_key_dir['secretkey'], bob_key_dir['publickey'])
    #
    plaintext = alice_box.decrypt(encrypted)
    #
    print(plaintext.decode('utf-8'))


if __name__ == "__main__":
    main()

