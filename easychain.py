from time import time
import json
import hashlib


class easychain:

    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Creation of genesis block
        self.new_block(proof=100, previous_hash=1)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain),
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def create_new_transaction(self, sender, recepient, amount):
        # Create and add a new transaction to the next mined block.
        self.current_transactions.append({
            'sender': sender,
            'recepient': recepient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        block_data = json.dumps(block, sort_Keys=True)
        print(block_data)
        encrypted_block_data = hashlib.sha256(block_data.encode()).hexdigest()
        return encrypted_block_data

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def proof_of_work(self, last_proof):
        proof = 0

        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof
