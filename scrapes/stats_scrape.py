from bs4 import BeautifulSoup as bs
import csv

dept = "stats"

in_file = "htmls/" + dept + "_fac_list.html"
out_file = "depts/" + dept + ".tsv"

DEPT = dept.upper()
no_mi = "-"

with open(in_file, 'r') as html_doc:
	soup = bs(html_doc)

names = soup.findAll("td", { "class" : "views-field views-field-field-url"})

with open(out_file, 'w+') as out:
	writer = csv.writer(out, delimiter="\t")
	for f in names:
		row = []
		name = f.p.a.text.strip().split(" ") ## returns itemized name list
		title = f.em.text.strip()

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