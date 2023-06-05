
import ipfshttpclient
import json
from web3 import Web3

api = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
new_file = api.add('circles.png')

ganache_url = "http://127.0.0.1:7545"
web3_var = Web3 (Web3.HTTPProvider(ganache_url))
print(web3_var.isConnected())
print(web3_var.eth.block_number)

web3_var.eth.defaultAccount = web3_var.eth.accounts[0] #it means that this contract is gonna apply for this account

abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"getGreetings","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greetings","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreetings","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
address = web3_var.toChecksumAddress( "0xc8a0d7a3B0C29B90965458357Fd8442A45bA1635")

contract =  web3_var.eth.contract(address=address , abi = abi)

print("Previous Hash : {}".format(
    contract.functions.getHash().call()
))

tx_hash = contract.functions.setHash(new_file['Hash']).transact()

web3_var.eth.waitForTransactionReceipt(tx_hash)
print("Current Hash : {}".format(
    contract.functions.getHash().call()
))
