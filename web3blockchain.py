from web3 import Web3
import json
# putting endpoint here 
# Part 1 
# infura_url = "https://mainnet.infura.io/v3/40645766d72a44218675029469137f90"
# web3 = Web3(Web3.HTTPProvider(infura_url))
# print(web3.isConnected())
# print(web3.eth.blockNumber)

# Now making connection with a sm art contract
# Part2 how to enteract with smart contract and get data 
# abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"}]')  #its a kind of json array that describes functions on the smart contract , its basically use for to talk to the smart contract
# address = "0xFe806862eF3F3852DdD757F910f04B81E6C62997"
# # now to talk with the etherium 

# contract = web3.eth.contract(address=address , abi = abi)
# totalSupply = contract.functions.totalSupply().call()
# print(web3.fromWei(totalSupply,"ether"))
# print(contract.functions.name().call())
# print(contract.functions.symbol().call())

# balance = contract.functions.balanceOf("0x442c003bA7a391A219EAb06D25dc2ADBb7392098").call()
# print(web3.fromWei(balance,"ether"))

# Part3  sending transactions on etherium
# for this we will use ganache which is free and we must n8 have worries for being losing our money

ganache_url = "http://127.0.0.1:7545"
web3 = Web3 (Web3.HTTPProvider(ganache_url))
print(web3.isConnected())
print(web3.eth.block_number)

# Now inorder to make transictions we need both accounts 

account_1 = "0x1069f315EB44778fEC8E050feAd9AFa42Fb87A0a"
account_2 = "0xE0c9F4B54c3ab436Ab37f0C58BBb41f0Bab5DBAc"
private_Key_of_account1 = "0x9f9743ae4e121e4b8effda9541637162a18aa24f642130364213b258408ab7c1"
#Get the nonce 
nonce = web3.eth.getTransactionCount(account_1)
#  Build a transaction 
tx = {
    'nonce':nonce, # nonce provents you from sendin the transaction twice 
    'to': account_2 ,
    'value':web3.toWei(1,'ether'),
    'gas' : 200000 , #Gas is the amount you have to pay on each transaction
    'gasPrice':web3.toWei('50','gwei') #larger denomination of wei smaller than ethereum  
}
#  Signed the transactions
signed_tx = web3.eth.account.signTransaction(tx , private_Key_of_account1)
#  send transactions
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
#  get transaction hash
print(web3.toHex(tx_hash))






