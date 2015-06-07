from bs4 import BeautifulSoup as bs
import csv

dept = "med"

in_file = "htmls/" + dept + "_fac_list.html"
out_file = "depts/" + dept + ".tsv"

DEPT = dept.upper()
no_mi = "-"

with open(in_file, 'r') as html_doc:
	soup = bs(html_doc)

names = soup.findAll("div", { "class" : "node__content"})

count = 0

with open(out_file, 'w+') as out:
	writer = csv.writer(out, delimiter="\t")
	for f in names:
		row = []
		items = f.h2.a.text.strip().split(", ") ## splits on first and last
		name = items[1].split(" ") ## splits f / mi 
		name.append(items[0])
		title = f.h3.text.strip()

		## Handle Blank Title spot
		if(not title):
			title = "Professor"
		row.append(name[0]) ## first name
		if(len(name) == 2):
			## only first and last
			row.append(no_mi)
		if(len(name) > 3):
			## handle more than 3 names
			temp = ""
			for n in name[1:-1]:
				temp += n + " "
			row.append(temp.strip())
			row.append(name[-1])
		else:
			row.extend(name[1:]) ## mi and last

		row.extend([title, DEPT])
		print row
		count += 1
		writer.writerow(row)

print "\n\n\nSuccessfully wrote %d lines to %s\n\n" % (count, out_file)