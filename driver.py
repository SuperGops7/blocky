from blocky import Chain

chain = Chain()

t1 = chain.add_transaction("Vitalik", "Satoshi", 100)

t2 = chain.add_transaction("Satoshi", "Alice", 10)

t3 = chain.add_transaction("Alice", "Charlie", 34)

chain.add_block(12345)

t4 = chain.add_transaction("Bob", "Eve", 23)

t4 = chain.add_transaction("Dennis", "Brian", 3)

t6 = chain.add_transaction("Ken", "Doug", 88)

chain.add_block(6789)

print(chain.blockchain)