from time import time


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
