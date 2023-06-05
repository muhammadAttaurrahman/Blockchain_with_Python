import json
from web3 import Web3, contract 

#In this file we are gonna read and write A smart contract  

ganache_url = "http://127.0.0.1:7545"
web3_var = Web3 (Web3.HTTPProvider(ganache_url))
print(web3_var.isConnected())
print(web3_var.eth.block_number)

web3_var.eth.defaultAccount = web3_var.eth.accounts[0] #it means that this contract is gonna apply for this account

abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"getGreetings","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greetings","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreetings","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
address = web3_var.toChecksumAddress( "0x3dDE37A4F0575c0eF77dcEc73BB4CA3532EAC8d5")

contract =  web3_var.eth.contract(address=address , abi = abi)

print("Previous Greetings : {}".format(
    contract.functions.getGreetings().call()
))

tx_hash = contract.functions.setGreetings('Hello I am blockChain developer, And I am preparing myself for my research').transact()

web3_var.eth.waitForTransactionReceipt(tx_hash)
print("Updated Greetings : {}".format(
    contract.functions.getGreetings().call()
))

