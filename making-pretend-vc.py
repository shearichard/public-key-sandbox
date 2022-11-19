import nacl.utils
from nacl.public import PrivateKey, Box
import pprint
import base64

def make_verified_credential():
    verified_cred_as_json = {'name': 'Alice', 'age': 22}
    verified_cred_as_str = str(verified_cred_as_json)
    verified_cred_as_bytes = str.encode(verified_cred_as_str)

    return verified_cred_as_bytes


def make_key_pair(for_who):
    secret_key = PrivateKey.generate()
    public_key = secret_key.public_key
    return {'key_pair_owner': for_who, 'secretkey': secret_key, 'publickey': public_key}


def main():
    # Make key pairs for the Verified Credential Issuer and Verified Credential Holder
    issuer_key_dir = make_key_pair('Issuer')
    holder_key_dir= make_key_pair('Holder')

    # Make a PyNacl Box for Issuer and Holder (https://pynacl.readthedocs.io/en/latest/public/#nacl-public-box)
    holder_box = Box(holder_key_dir['secretkey'], issuer_key_dir['publickey'])
    issuer_box = Box(issuer_key_dir['secretkey'], holder_key_dir['publickey'])

    # Create Verified Credential and encrypted them using holders public key
    verified_cred_as_bytes = make_verified_credential()
    encrypted_verified_cred = holder_box.encrypt(verified_cred_as_bytes)
    #
    # Unencrypt Verified Credential to demonstrate the fully cycle 
    unencrypted_verified_cred_A = issuer_box.decrypt(encrypted_verified_cred)
    
    #Dump intermediate and final data
    print("")
    print("Verified Credential before encryption ...")
    print(verified_cred_as_bytes)
    print("")
    print("Verified Credential after encryption ...")
    print(encrypted_verified_cred)
    print("")
    print("Verified Credential after decryption ...")
    print(unencrypted_verified_cred_A.decode('utf-8'))


if __name__ == "__main__":
    main()

