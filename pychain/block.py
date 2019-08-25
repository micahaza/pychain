""" One block. 
    TODO: proof might be removed as other than PoW consensuses should be implemented
"""
from time import time

class Block(object):
    """Represents a single block of the blockchain
    
    Attributes:
        :index: Index of this block, sequential
        :previous_hash: Hash of the previous block in the blockchain
        :timestamp: Timestamp of the block
        :transactions: List of transactions which are included in the block
        :proof: The proof of work number that yielded this block
    """
    def __init__(self, index, previous_hash, transactions, proof, timestamp=time()):
        self.index = index
        self.hash = None
        self.previous_hash = previous_hash or None
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof

    def __repr__(self):
        return str(self.__dict__)

