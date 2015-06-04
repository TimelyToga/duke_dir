import csv

complete = []
incomplete = []

with open('dept_list.csv', 'rw') as f:
	reader = csv.reader(f, delimiter='	')
	for row in reader:
		print row
		if(row[1] == '-'):
			incomplete.append(row[0])
		else:
			complete.append(row[0])

	tot_len = len(complete) + len(incomplete)
	print "\n\nCOMPLETE: (%d/%d)\n" % (len(complete), tot_len)
	for a in complete:
		print a

	print "\n\nINCOMPLETE: (%d/%d)\n" % (len(incomplete), tot_len)
	for a in incomplete:
		print a