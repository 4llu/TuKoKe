import generate
import json
import sys
from parameters import *

# PEOPLE_SETS = 2 # Debug
# REPETITIONS = 3 # Debug
# TIMESTEPS = 2 # Debug
PEOPLE_SETS = 5
REPETITIONS = 10
TIMESTEPS = 30

# Parameter set number
param_sets_start = int(sys.argv[1])
param_sets_stop = int(sys.argv[2])


# Newsfeed
sites  = generate.sites()
# Filter
filter = generate.filter()


##### Main loop #####

# Parameter sets
# =============================
for param_num in range(param_sets_start, param_sets_stop):
	# Save everything here
	parameter_results = []

	# Friend sets
	# ======================================
	for popSet in range(PEOPLE_SETS):
		# Save results of population set here
		population_results = []
		# Create people
		people = generate.people(param_num)
		generate.friends(people, param_num)

		# Repetitions
		# ======================================
		for rep in range(REPETITIONS):
			# Save results of repetition here
			rep_results = []

			# Single run
			# =======================================
			for step in range(TIMESTEPS):

				print(step) # Debug

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
				# print(people[0].received)
				# print(people[0].seen)
				# print(people[0].interests)

			# Repetition result save
			for person in people:
				person_results = {};
				person_results["received"] = person.received
				person_results["seen"] = person.seen
				# person_results["created"] = person.created
				# person_results["shared"] = person.shared
				person_results["interests"] = person.interests
				# person_results["preference"] = person.preference
				rep_results.append(person_results)
			population_results.append(rep_results)

			# Reset people
			for person in people:
				person.reset()

			print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||") # DEBUG

		# People set result save
		parameter_results.append(population_results)

	#Save results with JSON
	with open("Results/results" + str(param_num) + ".json", "w") as f:
		f.write(json.dumps(parameter_results))
	with open("Results/params" + str(param_num) + ".json", "w") as f:
		params = [FILTER_ON[param_num], F_MEAN[param_num], F_DEVIATION[param_num], PSHARE[param_num], PCREATE[param_num]]
		f.write(json.dumps(params))
