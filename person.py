class Person:
	def __init__(self, id, interests, friends, pShare, pCreate):
		# From parameters
		self.id = id
		self.interests = interests
		self.friends = friends
		self.pShare = pShare
		self.pCreate = pCreate
		# Init otherwise
		self.received = {}
		self.seen = {}
		self.created = {}
		self.shared = {}
		for ii in self.interests:
			self.received[ii[0]] = [0, 0, 0]
			self.seen[ii[0]] = [0, 0, 0]
			self.created[ii[0]] = [0, 0, 0]
			self.shared[ii[0]] = [0, 0, 0]
		self.buffer = []
		self.outbox = []

	def seePosts(self, filter):
		# Save received
		for post in self.buffer:
			self.received[post.topic][post.type] += 1
		# Filter
		self.buffer = filter.filter(self.buffer)
		# Save seen
		for post in self.buffer:
			self.seen[post.topic][post.type] += 1
