from bs4 import BeautifulSoup as bs
import csv

dept = "law"

in_file = "htmls/" + dept + "_fac_list.html"
out_file = "depts/" + dept + ".tsv"

DEPT = dept.upper()
no_mi = "-"

with open(in_file, 'r') as html_doc:
	soup = bs(html_doc)

names = soup.findAll("div", { "class" : "directorydescription"})

count = 0

with open(out_file, 'w+') as out:
	writer = csv.writer(out, delimiter="\t")
	for f in names:
		row = []
		name = f.h3.a.text.strip().split(" ") ## splits name into respective pieces

		## Handle no title
		try:
			title = f.p.text.strip()
		except:
			title = "Professor"

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
		writer.writerow([unicode(s).encode("utf-8") for s in row])

print "\n\n\nSuccessfully wrote %d lines to %s\n\n" % (count, out_file)