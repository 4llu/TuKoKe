from random import random as rr

class Filter:
		def __init__(self):
			pass
			
		def filter(self, buffer, interests, preference):
			ret = []
			bonus = 0
			for post in buffer:
				if post.preference != 0:
					if post.preference == preference:
						bonus = 0.1
					else:
						bonus = 0.1
				if rr() < interests[post.topic]:
					ret.append(post)
			return ret
