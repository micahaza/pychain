import pytest, os
from pychain.block import Block
from pychain.wallet import Wallet

def pytest_sessionstart(session):
    pass

def pytest_sessionfinish(session, exitstatus):
    try:
        os.remove('tests/test1.wal')
        os.remove('tests/test2.wal')
    except OSError:
        pass

@pytest.fixture(scope='module')
def block():
    b = Block(1, '', [], 100)
    yield b

@pytest.fixture(scope='module')
def wallet():
    yield Wallet()
