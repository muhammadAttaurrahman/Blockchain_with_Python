from web3 import Web3
import json
# putting endpoint here 
# Part 1 
infura_url = "https://mainnet.infura.io/v3/40645766d72a44218675029469137f90"  #EndPoint in the project 
web3_var = Web3(Web3.HTTPProvider(infura_url))
print(web3_var.isConnected())
print(web3_var.eth.blockNumber)



# infura is bisacally an ethereum as a node service ,  it provides access to the ethereum network
#  And web3 is used for talking to Bloackchain using python

