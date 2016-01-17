from random import choice as rc
from random import randint as ri
from random import random as rr
from random import gauss
import math

from constants import *
from parameters import *
from filter import Filter
from person import Person
from filter import Filter
from sites import Site


def sites():
	sites = []
	# Create sites for all topics
	for ii, topic in enumerate(TOPICS):
		# Split topic
		if ii == 0:
			sites.append(Site(topic, S_MEAN / 2, S_DEVIATION / 2, 1))
			sites.append(Site(topic, S_MEAN / 2, S_DEVIATION / 2, 2))
		# Rest
		else:
			sites.append(Site(topic, S_MEAN, S_DEVIATION, 0))

	return  sites

def filter(param_num):
	return Filter(FILTERMAX[param_num])

def people(param_num):
	people = []
	# Create people
	for ii in range(PEOPLE):
		new_person = Person(PSHARE[param_num], PCREATE[param_num], DOI, param_num)
		new_person.reset() # Init
		people.append(new_person)

	# Create quotas
	quotas = []
	for ii, topic in enumerate(TOPICS):
		quotas.append(math.ceil(PEOPLE * I_CONF[ii]))

	# Distribute interests
	for ii, quota in enumerate(quotas):
		for nn in range(quota):
			# Interested or very interested
			d = DOI[0] if rr() < DOI_PREF else DOI[1]

			# Pick a suitable person. Pick any person after 3 tries.
			person = 0 # Init
			for jj in range(3): # HARDCODE 3
				person = ri(0, PEOPLE - 1)
				# Count previus topics of interest
				num = 0
				for interest in people[person].interests.values():
					if interest != 0:
						num += 1
				# Give new interest if few previous interests
				if num < 2: # HARDCODE 2
					people[person].interests[TOPICS[ii]] = d
					break
				# Smaller chance to get many interests
				elif rr() < 0.3: # HARDCODE 0.3
					people[person].interests[TOPICS[ii]] = d
					break
			# Anyone goes
			else:
				person = ri(0, PEOPLE -1)
				people[person].interests[TOPICS[ii]] = d

			# Split topic
			if (ii == 0):
				# Preferences go half and half
				people[person].preference = 1 if nn % 2 == 0 else 2

	return people

def friends(people, param_num):
	for ii, person in enumerate(people):
		# Send friend requests
		for nn in range(int(gauss(F_MEAN[param_num], F_DEVIATION[param_num]))):
			# Pick a person
			id = ri(0, PEOPLE - 1)
			# Skip self
			if id == ii:
				continue
			other_person = people[id]

			# Logic of accepting a friend request
			# Amount of previous friends
			# HARDCODE All numbers
			if len(other_person.friends) < 4 or (len(other_person.friends) < 8 and rr() < 0.7) or rr() < 0.3:
				prob = 0.3
				# Mutual interests
				for jj, topic in enumerate(TOPICS):
					# Split topic
					if jj == 0:
						# No preference
						if other_person.preference == 0 or person.preference == 0:
							pass
						# Same preference
						elif person.preference == other_person.preference:
							# Shared interest
							prob += 0.3
							# Bonus
							prob += 0.1
						# Different preference
						else:
							# Penalty
							prob -= 0.1
					# Rest
					else:
						# Shared interest
						if other_person.interests[topic] > 0 and person.interests[topic] > 0:
							prob += 0.3
				# Accept of decline friend request
				if rr() < prob:
					person.friends.append(id)
					other_person.friends.append(ii)
