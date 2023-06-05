from web3 import Web3 
import json

ganache_url = "http://127.0.0.1:7545"
web3_var = Web3 (Web3.HTTPProvider(ganache_url))
print(web3_var.isConnected())
print(web3_var.eth.block_number)
# Now inorder to make transictions we need both accounts 

account_1 = "0x5EA5d2abf27a955127afCc4c3666b2FF6C422b1c"
account_2 = "0xa19e09C7bE0F2D33ef475f111ca0f8C9A57D736b"
private_Key_of_account1 = "0948f122b84326b058184c826bcbc9fe0e110d43cc3b2b51d84cdf53f6418360"
#Get the nonce 
nonce = web3_var.eth.getTransactionCount(account_1)
#  Build a transaction 
tx = {
    'nonce':nonce, # nonce provents you from sending the transaction twice 
    'to': account_2 ,
    'value':web3_var.toWei(3,'ether'),
    'gas' : 3000000 , #Gas is the amount you have to pay on each transaction
    'gasPrice':web3_var.toWei('50','gwei') #larger denomination of wei smaller than ethereum  
}
#  Signed the transactions
signed_tx = web3_var.eth.account.signTransaction(tx , private_Key_of_account1)
#  send transactions
tx_hash = web3_var.eth.sendRawTransaction(signed_tx.rawTransaction)
#  get transaction hash
print(web3_var.toHex(tx_hash))