from random import random as rr
from random import randint as ri
from post import Post
from constants import TOPICS
from parameters import FILTER_ON
from parameters import BONUS_ON

class Person:
	def __init__(self, pShare, pCreate, DoI, param_num):
		# From parameters
		self.pShare = pShare
		self.pCreate = pCreate
		self.DoI = DoI
		self.param_num = param_num
		# Add/fill/change later
		self.interests = {}
		for topic in TOPICS:
			self.interests[topic] = 0
		self.friends = []
		self.preference = 0 # 0: topic not of interest, 1: one side, 2: the other side

	def reset(self):
		self.buffer = []
		self.outbox = []
		# To save results
		self.received = {}
		self.seen = {}
		self.created = {}
		self.shared = {}
		for ii in self.interests:
			# type as [site, created, shared]
			if ii == "A":
				# [same pref, different pref]
				self.received[ii] = [[0, 0], [0, 0], [0, 0]]
			else:
				self.received[ii] = [0, 0, 0]
			if ii == "A":
				self.seen[ii] = [[0, 0], [0, 0], [0, 0]]
			else:
				self.seen[ii] = [0, 0, 0]
			self.created[ii] = [0, 0, 0]
			self.shared[ii] = [0, 0, 0]

	def getPosts(self, site):
		# Preference bonus
		bonus = 0
		if BONUS_ON[self.param_num]:
			if site.preference == self.preference:
				bonus = 0.2
			elif site.preference != 0:
				bonus = -0.2
			# Prevent negative interest
			if self.interests[site.topic] + bonus < 0:
				bonus = 0
		num = int(len(site.posts) * (self.interests[site.topic] + bonus))
		for post in site.posts[:num]:
			self.buffer.append(post)

	def seePosts(self, filter):
		# Save received
		for post in self.buffer:
			if post.topic == "A":
				if self.preference == post.preference:
					self.received[post.topic][post.type][0] += 1
				else:
					self.received[post.topic][post.type][1] += 1
			else:
				self.received[post.topic][post.type] += 1
		# Filter
		if FILTER_ON[self.param_num]:
			self.buffer = filter.filter(self.buffer, self.interests)
		# Save seen
		for post in self.buffer:
			if post.topic == "A":
				if self.preference == post.preference:
					self.seen[post.topic][post.type][0] += 1
				else:
					self.seen[post.topic][post.type][1] += 1
			else:
				self.seen[post.topic][post.type] += 1

	def share(self):
		for post in self.buffer:
			# Probability of sharing and skip posts of opposite preference
			if rr() < self.pShare and (post.preference == 0 or post.preference == self.preference):
				# Create new post for sharing
				pref = 0
				# Add preference if necessary
				if post.topic == TOPICS[0]:
					pref = self.preference
				self.outbox.append(Post(post.topic, 2, pref))

	def create(self):
		for topic in self.interests:
			# Check if interested
			if self.interests[topic] != 0:
				# To create or not to create
				if rr() < self.pCreate:
					# Create
					for ii in range(ri(0, 3)): # HARDCODE (0, 3)
						# Add preference if necessary
						pref = 0
						if topic == TOPICS[0]:
							pref = self.preference
						self.outbox.append(Post(topic, 1, pref))

	def send(self, people):
		for friend in self.friends:
			for post in self.outbox:
				people[friend].buffer.append(post)
		self.outbox = []
