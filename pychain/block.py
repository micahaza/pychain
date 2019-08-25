""" One block. 
    TODO: proof might be removed as other than PoW consensuses should be implemented
"""
from time import time
import rlp

class Block(rlp.Serializable):
    """Represents a single block of the blockchain
    
    Attributes:
        :index: Index of this block, sequential
        :previous_hash: Hash of the previous block in the blockchain
        :timestamp: Timestamp of the block
        :transactions: List of transactions which are included in the block
        :proof: The proof of work number that yielded this block
    """
    fields = (
        ('index', rlp.sedes.big_endian_int),
        ('previous_hash', rlp.sedes.text),
        ('timestamp', rlp.sedes.big_endian_int)
    )

    def __init__(self, index, previous_hash, transactions, proof, timestamp=time(), **kwargs):
        super().__init__(index=index, previous_hash=previous_hash, timestamp=timestamp, **kwargs)
        # self.index = index
        self.hash = None
        self.transactions = transactions
        self.proof = proof

    def __repr__(self):
        return str(self.__dict__)

    def create_genesis_block(self):
        super().serialize()
