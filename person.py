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

	def getPosts(self, site):
		num = int(site.posts.length * interests[site.topic])
		for post in site.posts[:num]:
			self.buffer.append(post)

	def seePosts(self, filter):
		# Save received
		for post in self.buffer:
			self.received[post.topic][post.type] += 1
		# Filter
		if filter:
			self.buffer = filter.filter(self.buffer)
		# Save seen
		for post in self.buffer:
			self.seen[post.topic][post.type] += 1

	def share(self):
		# FIXME Not very scientific is it?
		for post in self.buffer:
			# Interested or very interested
			# FIXME 0.4 modified to final scale for degrees of interest
			if interests[post.topic] > 0.4:
				# To share or not to share
				if random.random() < pShare:
					# Mark as shared
					post.type = 2
					self.outbox.append(post)

	def create(self):
		# FIXME "Empirically found to be suitable"
		for topic in interests:
			# Interested or very interested
			# FIXME 0.4 modified to final scale for degrees of interest
			if interests[topic] > 0.4:
				# To create or not to create
				if random.random() < pCreate:
					# Create 1 or 2
					#FIXME Are 1 and 2 correct numbers
					for ii in range(random.randint(1, 2)):
						self.outbox.append(Post(topic, 1))


	def send(self):
		for friend in self.friends:
			for post in outbox:
				friend.buffer.append(outbox)
		self.outbox = []
