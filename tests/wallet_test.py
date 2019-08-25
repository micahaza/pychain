import ecdsa, os

def test_it_creates_a_wallet_object_with_empty_keys(wallet):
    assert wallet.private_key is None
    assert wallet.public_key is None

def test_it_generates_keys(wallet):
    wallet.create_keys()
    assert type(wallet.public_key) == ecdsa.keys.VerifyingKey
    assert type(wallet.private_key) == ecdsa.keys.SigningKey

def test_it_saves_wallet_file(wallet):
    wallet.save_keystore('tests/test1.wal')
    assert os.path.isfile('tests/test1.wal') == True

# TODO make sure it loads the correc one, checking type is simply not enough
def test_it_can_load_saved_wallet_file(wallet):
    wallet.create_keys()
    wallet.save_keystore('tests/test2.wal')
    wallet.load_keystore('tests/test1.wal')
    assert type(wallet.public_key) == ecdsa.keys.VerifyingKey
    assert type(wallet.private_key) == ecdsa.keys.SigningKey
    wallet.load_keystore('test2.wal')
    assert type(wallet.public_key) == ecdsa.keys.VerifyingKey
    assert type(wallet.private_key) == ecdsa.keys.SigningKey

def test_it_can_sign_a_message(wallet):
    msg = 'Sign me please'
    signature = wallet.sign(msg)
    assert signature is not None
    assert type(signature) == bytes

def test_it_can_verify_signed_message(wallet):
    msg = 'Sign me please'
    signature = wallet.sign(msg)
    assert wallet.verify(msg, signature) == True

def test_it_returns_false_if_signature_is_not_valid(wallet):
    wallet.create_keys()
    msg = 'Sign me please'
    signature = wallet.sign(msg)
    assert wallet.verify('Sign me please, I am malicious', signature) == False