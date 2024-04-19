import json
import pickle  
import BlockChain
from BlockChain import BlockChain
from BlockChain import Block



def load(email):

    try:
        
        with open('Models/Transactions.pkl', 'rb') as f:
            obj = pickle.load(f)
        print(obj.chain)
        r=[]
        for l in obj.chain:
            m={}
            print(l.data[0]['recipient_email'],'<<<<<<<<<<<<<')
            if email==l.data[0]['recipient_email']:
                m['tid']=l.data[0]['transaction_id']
                m['semail']=l.data[0]['sender_email']
                m['sname']=l.data[0]['sender_name']
                m['ts']=l.data[0]['timestamp']
                r.append(m)
                
        
        #r.remove('genesis')
        print(r)
        return r
    except Exception as e:
        print(e,'<<<<')

        return []


if __name__ == '__main__':
    print(load('sajid@gmail.com'))