
def test_block_creation(block):
    assert block.index == 1
    assert block.hash == None
    assert block.previous_hash == None
    assert block.transactions == []