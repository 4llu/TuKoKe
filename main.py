# Constants
from constants import TIMESTEPS
import generate

PEOPLE_SETS = 3 # HARDCODE
REPETITIONS = 5 # HARDCODE

# Newsfeed
sites  = generate.sites()
# Filter
filter = generate.filter()

##### Main loop #####

### Different friend sets with same parameters ###
for pop range(PEOPLE_SETS):
	# Create people and distribute interests
	people = generate.people()
	# Create friend network
	generate.friends(people)
	### Repetitions (because of stochasticity) ###
	for rep in range(REPETITIONS):
		#---- Single run ----#
		for step in range(TIMESTEPS):
			# Create posts
			for site in sites:
				site.createPosts()

			# Get and send posts
			for person in people:
				# From sites
				for site in sites:
					person.getPosts(site)
				# Give other people
				person.send()

			# Process posts
			for person in people:
				person.seePosts(filter)
				person.share()
				person.create()
				person.buffer = []

		# TODO Save results

# print people[0].received
