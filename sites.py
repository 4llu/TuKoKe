from random import gauss
from post import Post

class Site:
	def __init__(self, topic, mean, deviation):
		self.topic = topic
		self.mean = mean
		self.deviation = deviation
		self.posts = []

	def createPosts(self):
		num = int(gauss(self.mean, self.deviation))
		for ii in range(num):
			self.posts.append(Post(self.topic, 0))
