class Blockchain(object):
	def __init__(self):
		# Creates an initial empty list to store our blockchain
		self.chain = []
		self.current_transactions = []

	def new_block(self):
		# Creates a new Block and adds it to the chain
		pass

	def new_transaction(self, sender, recipient, amount):
		"""
		Adds a new transaction to the list of transactions
		
		:param sender: <str> Address of the Sender
		:param recipient: <str> Address of the Recipient
		:param amount: <int> Amount
		:return: <int> The index of the Block that will hold this transaction
		"""

		self.current_transactions.append({
			'sender': sender, 
			'recipient': recipient, 
			'amount': amount, 
		})
		

	@staticmethod
	def hash(block):
		# Hashes a Block
		pass

	@property
	def last_block(self):
		# Returns the last Block in the chain