from bs4 import BeautifulSoup as bs
import csv

dept = "theater"

in_file = "htmls/" + dept + "_fac_list.html"
out_file = "depts/" + dept + ".tsv"

DEPT = dept.upper()
no_mi = "-"

with open(in_file, 'r') as html_doc:
	soup = bs(html_doc)

names = soup.findAll("div", { "class" : "fac-info"})

with open(out_file, 'w+') as out:
	writer = csv.writer(out, delimiter="\t")
	for f in names:
		row = []
		name = f.h4.a.text.strip().split(" ") ## returns itemized name list
		title = f.h5.text.strip()

		## Handle Blank Title spot
		if(not title):
			title = "Professor"
		row.append(name[0]) ## last name
		if(len(name) == 2):
			## only first and last
			row.append(no_mi)
		row.extend(name[1:]) ## first and mi

		row.extend([title, DEPT])
		print row
		writer.writerow(row)