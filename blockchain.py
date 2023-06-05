import  hashlib 

#Simple BlockChain in python 
class piCoinchain :
    def __init__(self , previous_block_hash , transaction_list):
        
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        
        self.block_data = previous_block_hash+"\n" + "-".join(transaction_list)  #concatenation
        self.current_block_hash = hashlib.sha256(self.block_data.encode()).hexdigest() #To generate Hash 

#Transactions details to be stored

t1 = "Ali sends 2 picoin to Maaz"
t2 = "Maaz sends 2.8 picoin to Nawaz"
t3 = "Nawaz sends 4 picoin to Rehman"
t4 = "Rehman sends 6 picoin to Ali"
t5 = "Ali sends 3.4 picoin to Nawaz"
t6 = "Rehman sends 1.4 picoin to Maaz"

# If we make any changes in above Transactions , so the current hash of the block will also be change

print("Initial Block")
intial_block =piCoinchain ("00000000000000000000 " , [t1 ,t2 ])  #Gensis Block , the previous Hash here is null 

print(intial_block.block_data)
print(intial_block.current_block_hash)

print("Second Block")
second_block =piCoinchain (intial_block.current_block_hash, [t3 ,t4 ])

print(second_block.block_data)
print(second_block.current_block_hash)

print("Third Block")
third_block =piCoinchain (second_block.current_block_hash, [t5 ,t6 ])

print(third_block.block_data)
print(third_block.current_block_hash)



