from nacl.signing import SigningKey

MESSAGE_TO_SIGN = b"Time for tea"

# Generate a new random signing key
signing_key = SigningKey.generate()

# Sign a message with the signing key
signed = signing_key.sign(MESSAGE_TO_SIGN)
type(signed)

# Obtain the verify key for a given signing key
verify_key = signing_key.verify_key

# Serialize the verify key to send it to a third party
verify_key_bytes = verify_key.encode()
#
print(MESSAGE_TO_SIGN)
print(verify_key_bytes)
