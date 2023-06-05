import  hashlib 
import json
from datetime import datetime

# Block class creation 

class Block :
    
    def __init__(self,index , previous_hash , current_transactions , timestamp , nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.current_transactions = current_transactions
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.compute_hash()
        
    # Returning current hash
    def compute_hash(self):
        block_string = json.dumps(self.__dict__,sort_keys=True)
        first_hash = hashlib.sha256(block_string.encode()).hexdigest()
        actual_hash = hashlib.sha256(first_hash.encode()).hexdigest()
        return actual_hash
    
    # Return dictionry
    def __str__(self):
        return str(self.__dict__)    
    

# Now to create the actual peer to peer chain 

class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.genesis_block()
    
    
    # Now to create Gensis Block
    def genesis_block(self):
        genesis_block = Block("Gensis",0x0 ,[3,4,5,6,7],'datetime.datetime.now().timestamp()',0)
        genesis_block.hash=genesis_block.compute_hash()
        self.chain.append(genesis_block.hash)
        self.transactions.append(str(genesis_block.__dict__))
        return genesis_block
    
    def getLastBlock(self):
        return self.chain[-1]
    
    # now we have to create function for nonce (defficulty)
    def proof_of_work(seld , block):
        defficulty = 1
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not (computed_hash.endswith('0' * defficulty) and ('55' * defficulty) in computed_hash):
            block.nonce +=1
            computed_hash = block.compute_hash()
            return computed_hash
        
    
    # Now to add a block to the chain
    def add(self ,data):
        block = Block(len(self.chain),self.chain[-1],data , 'datetime.now().timestamp',0)
        block.hash = self.proof_of_work(block)
        self.chain.append((block.hash))
        self.transactions.append(block.__dict__)
        return json.loads(str(block.__dict__).replace('\'','\"'))
    
    # now we have to create a transaction method as well for all transactions 
    def get_transactions(self,id):
        labels = ['Manufaturer' , 'Transportation' , 'Retailer']
        # while True:
        #     try:
        #         if id == 'all' :
        #             for i in range(len(self.transactions)-1):
        #                 print('{}:\n{}\n'.format(labels[i],self.transactions[i+1]))
        #                 break
        #         elif type(id) == int:
        #             print(self.transactions[id])
        #             break
        #     except Exception as e :
        #         print(e)
    
        while True:
            try:
                if id == 'all':
                    for i in range(len(self.transactions)-1):

                        print('{}:\n{}\n'.format(labels[i],self.transactions[i+1]))

                    break
                elif type(id) == int:

                    print(self.transactions[id])

                    break

            except Exception as e:

                print(e)
                

# Now here is transactions method 
def main ():
    manufacturer= {
        'transactions':
            [
                {
                    'timestamp':datetime.now().timestamp(),
                    'product_id':1,
                    'product_serial':50001000,
                    'name':'cotton pants',
                    'from':'Manufacturer X',
                    'to':'transportation X',
                    'message':'This product is in good order',
                    'digital_signature':'approved',
                    'flagged':'N'
                    
                },
                {
                    'timestamp':datetime.now().timestamp(),
                    'product_id':2,
                    'product_serial':50002000,
                    'name':'cotton pants',
                    'from':'Manufacturer X',
                    'to':'transportation X',
                    'message':'This product is in good order',
                    'digital_signature':'approved',
                    'flagged':'N'
                
                },
            ]
    }
    
    transportation = {
        'transactions' :
            [
                {
                    
                    'timestamp':datetime.now().timestamp(),
                    'product_id':1,
                    'product_serial':50001000,
                    'name':'cotton pants',
                    'from':'Transportation X',
                    'to':'Retailer X',
                    'shifting_id':100,
                    'message':'This product is in good order ,shifted',
                    'digital_signature':'approved',
                    'flagged':'N'
                },
                {
                    'timestamp':datetime.now().timestamp(),
                    'product_id':2,
                    'product_serial':50002000,
                    'name':'cotton pants',
                    'from':'Transportation X',
                    'to':'Retailer X',
                    'shifting_id':101,
                    'message':'This product is damged ',
                    'digital_signature':'Retailer Review',
                    'flagged':'Y' 
                    
                },
                ]
    }
    
    retailer = {
        'transactions':
            [
                {
                    'timestamp':datetime.now().timestamp(),
                    'product_id':1,
                    'product_serial':50001000,
                    'name':'cotton pants',
                    'from':'Retailer X',
                    'to':'Retail shelf',
                    'Received_id':400,
                    'message':'This product is in good order ,Received',
                    'digital_signature':'approved',
                    'flagged':'N'
                },
                {
                    'timestamp':datetime.now().timestamp(),
                    'product_id':2,
                    'product_serial':50002000,
                    'name':'cotton pants',
                    'from':'Retailer X',
                    'to':'RTV',
                    'Receiving_id':401,
                    'message':'This product is damged ',
                    'digital_signature':'Rejected',
                    'flagged':'Y' 
                    
                },   
                
            ]
        }
    
            
#Now creating an instance of Blockchain class

    B = Blockchain()
    a=B.add(manufacturer)
    b = B.add(transportation)
    c=B.add(retailer)
    print(B.get_transactions('all'))

if __name__ == '__main__':
    main()                                
