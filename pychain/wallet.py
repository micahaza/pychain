import ecdsa
import base64
import json
import binascii

class Wallet:
    """Creates, loads and holds private and public keys.
        It can sign transactions and verify them.
    """
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def create_keys(self):
        private_key, public_key = self.generate_keys()
        self.private_key = private_key
        self.public_key = public_key

    def generate_keys(self):
        """Generate a new pair of private and public key."""
        # Private key
        private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        # Public key
        public_key = private_key.get_verifying_key()
        return(private_key, public_key)

    def save_keystore(self, filename):
        ks = {}
        ks['private_key'] = self.private_key.to_string().hex()
        ks['public_key'] = self.public_key.to_string().hex()
        try:
            with open(filename, "w") as f:
                f.write(json.dumps(ks))
        except(IOError):
            return "Could not save keystore file."
        return True

    def load_keystore(self, filename):
        try:
            with open(filename, "r") as f:
                z = json.loads(f.read())
        except(IOError):
            return "Could not load keystore file."
        self.public_key = ecdsa.VerifyingKey.from_string(binascii.unhexlify(z['public_key']), curve=ecdsa.SECP256k1)
        self.private_key = ecdsa.SigningKey.from_string(binascii.unhexlify(z['private_key']), curve=ecdsa.SECP256k1)
        return True

    def sign(self, payload):
        """Sign a message and return the signature.
        Arguments:
            :payload: Text which has to be signed
        """
        if not type(self.private_key) == ecdsa.keys.SigningKey:
            return None
        signature = self.private_key.sign(payload.encode())
        return signature

    def verify(self, payload, signature):
        """Tries to verify a payload with the given signature.
            Returns false if fails
        
        Arguments:
            :payload: Text which we want to verify.
            :signature: The signature which we want to verify the payload against.
        """
        try:
            return self.public_key.verify(signature, payload.encode())
        except(ecdsa.keys.BadSignatureError):
            return False
            
    def __repr__(self):
        return str(self.__dict__)