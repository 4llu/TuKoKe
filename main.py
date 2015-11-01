import random

import generator
import person
import filter
import site
import post


TIMESTEPS = 100

# Temporary generation process FIXME

### Sites
topics = ["A1", "A2", "B", "C", "D"]
sites = []
for topic in topics:
	sites.append(site(topic, 20, 5))

### Filter
filter = Filter(50)

### People
people = []

for ii in range(10):
	## Interests
	interests = {}
	topicsCopy = topics[:]
	# Very interested
	veryInterested = random.choice(topics)
	topicsCopy.remove(veryInterested)
	interests[veryInterested] = 0.8
	# Interested and mildly interested
	interest1 = random.choice(topics)
	topicsCopy.remove(interest1)
	interest2 = random.choice(topics)
	topicsCopy.remove(interest2)
	interests[interest1] = random.choice([0.3, 0.5])
	interests[interest2] = random.choice([0.3, 0.5])
	# The rest (not interested)
	for topic in topicsCopy:
		interests[topic] = 0

	## Friends
	friends = []

	## Create
	people.append(Person(ii, interests, friends, 0.2, 0.1))

# END of temporary generation process

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
		# Send to people
		person.send()

	# Process posts
	for person in people:
		person.seePosts()
		person.share()
		person.create()
		person.buffer = []
