from nacl.signing import SigningKey, VerifyKey
from nacl.exceptions import BadSignatureError

# Create a digital signature key pair
signing_key = SigningKey.generate()
verify_key = signing_key.verify_key

# Sign a message
message = b"Test message for digital signature"
signed_message = signing_key.sign(message)

# Verify the signed message
try:
    verify_key.verify(signed_message)
    print("Signature is valid.")
except BadSignatureError:
    print("Signature is invalid.")
