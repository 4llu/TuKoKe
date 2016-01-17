from random import gauss
from post import Post

class Site:
	def __init__(self, topic, mean, deviation, preference):
		self.topic = topic
		self.mean = mean
		self.deviation = deviation
		self.preference = preference
		self.posts = []

	def createPosts(self):
		self.posts = []
		num = int(gauss(self.mean, self.deviation))
		for ii in range(num):
			self.posts.append(Post(self.topic, 0, self.preference))
