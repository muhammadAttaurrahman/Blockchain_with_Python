# In this we are going to learn about how to interact with the blockchain 
# and look at the data in the block themselevs 

from web3 import Web3 
import json
import time as time

infura_url = 'https://mainnet.infura.io/v3/40645766d72a44218675029469137f90'
web3 = Web3 (Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)

# Now if you wanna have the complete info about the latest block 

latest = web3.eth.blockNumber 
# print(web3.eth.get_block(latest))

# Now if you wanna have information about multiple blocks 

for i in range (0 , 20):
    time.sleep(0.2)
    print ("\n\n *******************\n\n")
    time.sleep(0.5)
    print(web3.eth.get_block(latest-i))
    

# getting data from a specific block by its transaction

hash = '0xe0ccd7ef2245d3ca7d73d43fa3ab1994568c407020f2f1815349966b1d5a18e7'
print(web3.eth.getTransactionByBlock(hash , 1))







