from random import gauss
class Site:
	def __init__(self, topic, mean, deviation):
		self.topic = topic
		self.mean = mean
		self.deviation = deviation
		self.posts = []

	def createPosts(self):
		num = gauss(self.mean, self.deviation)
		for ii in num:
			self.posts.append(Post(self.topic, 0))
