from random import random as rr
from random import randint as ri
from post import Post

class Person:
	def __init__(self, id, interests, friends, pShare, pCreate, DoI):
		# From parameters
		self.id = id
		self.interests = interests
		self.friends = friends
		self.pShare = pShare
		self.pCreate = pCreate
		# Degree of interest
		self.DoI = DoI
		# Init otherwise
		self.received = {}
		self.seen = {}
		self.created = {}
		self.shared = {}
		for ii in self.interests:
			self.received[ii] = [0, 0, 0]
			self.seen[ii] = [0, 0, 0]
			self.created[ii] = [0, 0, 0]
			self.shared[ii] = [0, 0, 0]

		# Debug
		self.buffer = []
		self.outbox = []

	def getPosts(self, site):
		num = int(len(site.posts) * self.interests[site.topic])
		for post in site.posts[:num]:
			self.buffer.append(post)

	def seePosts(self, filter):
		# Save received
		for post in self.buffer:
			############### Debug #################
			# if post.type == 2:
			# 	print "lel"
			self.received[post.topic][post.type] += 1
		# Filter
		if filter:
			self.buffer = filter.filter(self.buffer, self.interests)
		# Save seen
		for post in self.buffer:
			self.seen[post.topic][post.type] += 1

	def share(self):
		for post in self.buffer:
			# Interested or very interested
			if self.interests[post.topic] >= self.DoI[1]:
				# To share or not to share
				if rr() < self.pShare:
					# Create new post for sharing
					self.outbox.append(Post(post.topic, 2))

	def create(self):
		for topic in self.interests:
			# Interested or very interested
			if self.interests[topic] >= self.DoI[1]:
				# To create or not to create
				if rr() < self.pCreate:
					# Create 1 or 2
					#FIXME What decides how many posts are created?
					for ii in range(ri(1, 2)):
						self.outbox.append(Post(topic, 1))

	def send(self):
		for friend in self.friends:
			for post in outbox:
				friend.buffer.append(outbox)
		self.outbox = []
