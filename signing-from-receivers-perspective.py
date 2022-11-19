from nacl.signing import VerifyKey


VERIFY_KEY_BYTES =b'v\x1d\xbe\xd6\xf7\x87\xfe\xa5m])\xd8\x87U\xe6j\\\xb8\xd6\xb8\x19\x06e@\xd4\x99\xf2\xc9\x11&\x8a\x04' 
SIGNED=b'v\x1d\xbe\xd6\xf7\x87\xfe\xa5m])\xd8\x87U\xe6j\\\xb8\xd6\xb8\x19\x06e@\xd4\x99\xf2\xc9\x11&\x8a\x04' 
# Create a VerifyKey object from a hex serialized public key
verify_key = VerifyKey(VERIFY_KEY_BYTES)

# Check the validity of a message's signature
# The message and the signature can either be passed together, or
# separately if the signature is decoded to raw bytes.
# These are equivalent:
print("Verify: Using method one - should pass")
verify_key.verify(SIGNED)

print("Mess up the signature")
# Alter the SIGNED message text
forged = SIGNED[:-1] + bytes([int(SIGNED[-1]) ^ 1])
# Will raise nacl.exceptions.BadSignatureError, since the signature check
# is failing
print("Verify: Using method one after corruption - should fail")
verify_key.verify(forged)
