from random import choice as rc

from constants import *
from filter import Filter
from person import Person
from filter import Filter
from sites import Site

def generate():

	# Create sites
	sites = []
	for topic in TOPICS:
		sites.append(Site(topic, MEAN, DEVIATION))

	# Create filter
	filter = Filter(FILTERMAX)

	# Create people
	# FIXME kind of random process atm
	people = []
	for ii in range(PEOPLE):
		## Interests
		interests = {}
		topicsCopy = TOPICS[:]
		# Very interested
		veryInterested = rc(topicsCopy)
		topicsCopy.remove(veryInterested)
		interests[veryInterested] = DOI[0]
		# Interested and mildly interested
		interest1 = rc(topicsCopy)
		topicsCopy.remove(interest1)
		interest2 = rc(topicsCopy)
		topicsCopy.remove(interest2)
		interests[interest1] = rc([DOI[1], DOI[2]])
		interests[interest2] = rc([DOI[1], DOI[2]])
		# The rest (not interested)
		for topic in topicsCopy:
			interests[topic] = 0

		# Friends
		# FIXME missing completely
		friends = []

		# Create person
		people.append(Person(ii, interests, friends, 0.2, 0.1, DOI))

	return sites, people, filter
