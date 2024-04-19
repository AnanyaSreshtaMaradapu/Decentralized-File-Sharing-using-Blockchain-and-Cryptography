
import json
import pickle  
import BlockChain
from BlockChain import BlockChain
from BlockChain import Block


def load():

    try:
        with open('models/ProteinSeqBC.pkl', 'rb') as f:
            obj = pickle.load(f)
        print(obj.chain)
        r=[]
        for l in obj.chain:
            print(l.data[0]['email'],'<<<<<<<<<<<<<')
            r.append(l.data[0]['protein'])
            
        
        r.remove('genesis')
        print(r)
        return r
    except Exception as e:
        print(e,'<<<<')

        return []


if __name__ == '__main__':
    load()