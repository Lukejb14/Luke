vowels = ('a', 'e', 'i', 'o', 'u')

def convert_word(word):
	firstletter = word[0]
	if firstletter in vowels:
		return word + "hay"
	else:
		return word[1:] + word[0] + "ay"


print "Please enter word."
text = raw_input()
print "====================================================="
print "Your word: " + text
print
print
print
print "Your word as piglatin:"
print convert_word(text)
print 
print
print
print
