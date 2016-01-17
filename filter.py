from random import random as rr
from constants import FILTERMAX

class Filter:
		def __init__(self, show):
			self.show = show

		def filter(self, buffer, interests):
			ret = []
			for post in buffer:
				if rr() < interests[post.topic]:
					ret.append(post)
			return ret
