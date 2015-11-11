import random

# Constants
from constants import *
# import generator
# Classes
from person import Person
from filter import Filter
from sites import Site

TIMESTEPS = 100

### FIXME Temporary generation process

### FIXME Topics
topics = ["A1", "A2", "B", "C", "D"]

sites = []

for topic in topics:
	# FIXME mean and deviation
	sites.append(Site(topic, 20, 5))

## FIXME Current Degree of Interest (DoI)
DoI = [0.8, 0.5, 0.3, 0]

### Filter
filter = Filter(50)

### People
people = []

for ii in range(10):

	## Interests
	interests = {}
	topicsCopy = topics[:]
	# Very interested
	veryInterested = random.choice(topicsCopy)
	topicsCopy.remove(veryInterested)
	interests[veryInterested] = DoI[0]
	# Interested and mildly interested
	interest1 = random.choice(topicsCopy)
	topicsCopy.remove(interest1)
	interest2 = random.choice(topicsCopy)
	topicsCopy.remove(interest2)
	interests[interest1] = random.choice([DoI[1], DoI[2]])
	interests[interest2] = random.choice([DoI[1], DoI[2]])
	# The rest (not interested)
	for topic in topicsCopy:
		interests[topic] = 0

	## Friends
	friends = []

	## Create
	people.append(Person(ii, interests, friends, 0.2, 0.1, DoI))

### END of temporary generation process

##### Main loop #####
for ii in range(TIMESTEPS):
	# Create posts
	for site in sites:
		site.createPosts()

	# Get posts
	for person in people:
		# From sites
		for site in sites:
			person.getPosts(site)
		# Send outbox to people
		person.send()

	# Process posts
	for person in people:
		person.seePosts(filter)
		person.share()
		person.create()
		person.buffer = []

### END

print people[0].received
