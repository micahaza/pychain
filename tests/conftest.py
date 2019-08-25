import pytest
from pychain.block import Block
from pychain.wallet import Wallet

@pytest.fixture(scope='module')
def block():
    b = Block(1, '', [], 100)
    yield b

@pytest.fixture(scope='module')
def wallet():
    yield Wallet()
