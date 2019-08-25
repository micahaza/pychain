from collections import OrderedDict

from utils.printable import Printable

class Transaction():
    """A single transaction which could be added to a block in the blockchain.
        TODO:  has to be decided which kind of signature we're going to use.
    Attributes:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :signature: The signature of the transaction.
        :amount: The amount of coins sent.
    """
    def __init__(self, sender, recipient, signature, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature

    def to_ordered_dict(self):
        """Converts this transaction into a (hashable) OrderedDict.
            This is important as we want the same result during hasing
            and dictionaries in python are not ordered.
        """
        return OrderedDict([('sender', self.sender), ('recipient', self.recipient), ('amount', self.amount)])

    def __repr__(self):
        return str(self.__dict__)        