print " "
print " "
print "Welcome to In-N-Out!"
#print "How many cheeseburgers would you like?"
print "Would you like a milkshake?    (1 = yes or 2 = no)"
response = int(raw_input())
if response == 1:
	print "How many milkshakes would you like?"
	milkshake = int(raw_input())
	print "How many cheeseburgers would you like?"
	burger = int(raw_input())
	milkshakep = milkshake * 2.16
	price = burger * 2.36 + milkshakep
	burger = str(burger)
	price = str(price)
	milkshake = str(milkshake)
	print " "
	print " "
	print "Lets review your order. You ordered " + burger + " burgers and " + milkshake + " milkshake(s)."
	print " "
	print "Your total is $" + price + "."
	print " "
	print " "
else:
	print "How many cheeseburgers would you like?"
	burger = int(raw_input())
	price = burger * 2.36
	burger = str(burger)
	price = str(price)
	print " "
	print " "
	print "Lets review your order. You ordered " + burger + " burgers."
	print " "
	print "Your total is $" + price + "."
	print " "
	print " "



#print "Lets review your order. You ordered" + burger + " burgers." "Your total is $" + price + "."
#print "You ordered " + burger + " " + "cheeseburgers"	