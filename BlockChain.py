import hashlib  
import json  
from time import time  
import pickle  
class Block:  
    def __init__(self, data, prev_hash):  
        self.data = data
        self.prev_hash = prev_hash
        self.hash=self.calc_hash()

    def calc_hash(self):  

        sha=hashlib.sha256()  
        print(str(self.data[0]['transaction_id'])+str(self.data[0]['sender_email'])+str(self.data[0]['recipient_email']))
        sha.update(str(str(self.data[0]['transaction_id'])+str(self.data[0]['sender_email'])+str(self.data[0]['recipient_email'])).encode('utf-8'))
        return sha.hexdigest()
        

class BlockChain:


    def __init__(self):  
        self.chain = [self.create_genesis_block()]


    def create_genesis_block(self):
        return Block([{'transaction_id':'genesis','sender_email':'genesis', 'sender_name':'genesis', 'recipient_email':'genesis'}],'00000000')


    def add_block(self, data):
        prev_block=self.chain[-1]
        new_block=Block(data, prev_block.hash)
        self.chain.append(new_block)


if __name__ == '__main__':
    bc=BlockChain()
    bc.add_block([{'transaction_id':'123','sender_email':'sajid@123','sender_name':'sajid','recipient_email':'ali@123' }])

    with open('models/Transactions.pkl', 'wb') as f:
        pickle.dump(bc, f,)
    print(bc.chain,'<<<<<<<<<<<<<<')
    
