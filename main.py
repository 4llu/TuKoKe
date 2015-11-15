# Constants
from constants import TIMESTEPS
from generator import  generate

sites, people, filter = generate()

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

# FIXME result processing
print people[0].received
