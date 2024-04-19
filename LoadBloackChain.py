import json
import pickle  
import BlockChain
from BlockChain import BlockChain
from BlockChain import Block



def load():

    try:

        with open('Models/Transactions.pkl', 'rb') as f:
            obj = pickle.load(f)
        print(obj.chain)
        d=dict({})

        i=1

        for l in obj.chain:
            #print(l.data[0]['transaction_id'])

            d[i]={'transaction_id':l.data[0]['transaction_id'],'sender_email':l.data[0]['sender_email'],'sender_name':l.data[0]['sender_name'],'recipient_email':l.data[0]['recipient_email'],'timestamp':l.data[0]['timestamp'], 'hash':l.hash, 'prev_hash':l.prev_hash}
            i=i+1

        y = json.dumps(d, indent=4)
        print(y)
        return y
    except Exception as e:
        print(e)

        return 'No Data Avaialble'
if __name__ == '__main__':
    print(load())