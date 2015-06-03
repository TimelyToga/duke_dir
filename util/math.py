import csv

DEPT = "MATHEMATICS"

with open("mathematics_test.csv", "r") as f:
	with open("math_out.csv", "w") as out:
		reader = csv.reader(f.read().splitlines())
		writer = csv.writer(out)
		for row in reader:
			new_row = []
			name = row[0].strip().split(" ")
			new_row.append(name[0])
			if(len(name) != 1):
				print name
				new_row.append(name[1].strip())
			for i in row[1:]:
				new_row.append(i.strip())
			new_row.append(DEPT)
			writer.writerow(new_row)