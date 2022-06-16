#!/usr/bin/python

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('dndroll'))
template = env.get_template('roller.html')

from random import randint
from dndroll import *
import sys
import os

getEnviron(subs)
loadClasses(subs)

try:
	roll = None
	eligibles = None
	
	for s in getStats(subs):
		eligibles = matchClasses(s,subs)
		if eligibles:
			roll = s
			break
	
	for s in roll:
		subs[s] = roll[s]
	
	subs['STATS'] = [(s,roll[s],"%+d" % (getMod(roll[s]))) for s in stats]
	
	subs['CLASSES'] = eligibles
	subs['ARGS'] = str(subs)
	subs['ROLES'] = getRoles(subs)
	subs['RACES'] = getRaces(subs)
	subs['BONUS'] = getBonus(subs)
	subs['DEFS'] = getDefenses(subs)
	subs['RULES'] = getRules(subs)
	subs['LINK'] = getLinkURL(subs)
		
except Exception, e:
	print "Exception",e


try:
	print template.render(subs)
	
except Exception,e:
	print "Failure with",e
