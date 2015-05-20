print "Welcome to the Los Angeles International Airport!"
print " "
print "How much does your suitcase weigh?"
suitcase = int(raw_input())
if suitcase < 50:
	print "Your suitcase is free of charge. Enjoy your flight!"

elif suitcase > 51:
	print "Your suitcase does not meet our luggague guidelines."
	print "Please pay an additional charge of $50"