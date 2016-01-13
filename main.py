# Constants
import generate
import json

PEOPLE_SETS = 4 # HARDCODE
REPETITIONS = 4 # HARDCODE
TIMESTEPS = 30 # HARDCODE

# Save results of parameter set here
par_results = []

# Newsfeed
sites  = generate.sites()
# Filter
filter = generate.filter()

##### Main loop #####

### Different friend sets with same parameters ###
for popSet in range(PEOPLE_SETS):
	# Save results of population set here
	pop_results = []
	# Create people and distribute interests
	people = generate.people()
	# Create friend network
	generate.friends(people)
	### Repetitions (because of stochasticity) ###
	for rep in range(REPETITIONS):
		# Save results of repetition here
		rep_results = []
		#---- Single run ----#
		for step in range(TIMESTEPS):
			print(step, "----------------------------------")
			# Create posts
			for site in sites:
				site.createPosts()

			# Get and send posts
			for person in people:
				# From sites
				for site in sites:
					person.getPosts(site)
				# Give other people
				person.send(people)

			# Process posts
			for person in people:
				person.seePosts(filter)
				person.share()
				person.create()
				person.buffer = []

			# DEBUG
			print(people[0].received)
			print(people[0].seen)
			print(people[0].interests)

		# Save results
		received = []
		seen = []
		created = []
		shared = []

		# Repetition result save
		for person in people:
			rep_results.append(person.received)
			rep_results.append(person.seen)
			rep_results.append(person.created)
			rep_results.append(person.seen)
		pop_results.append(rep_results)

		# Reset people
		for person in people:
			person.reset()
		print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||") # DEBUG

	#People set result save
	par_results.append(pop_results)
#Save results with JSON
with open("results.txt", "w") as f:
	f.write(json.dumps(par_results))
