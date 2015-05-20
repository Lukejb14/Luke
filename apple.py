import csv
with open("apple.csv", "rb") as f:
	reader = csv.reader(f)
	for column in reader:
			print column[4]