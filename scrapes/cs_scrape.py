from bs4 import BeautifulSoup as bs
import csv

dept = "cs"

in_file = "htmls/" + dept + "_fac_list.html"
out_file = "depts/" + dept + ".tsv"

DEPT = dept.upper()
no_mi = "-"

with open(in_file, 'r') as html_doc:
	soup = bs(html_doc)

names = soup.findAll("span", { "class" : "PeopleName"})

with open(out_file, 'w+') as out:
	writer = csv.writer(out, delimiter="\t")
	for f in names:
		row = []
		name = f.a.text.strip().split(" ") ## returns itemized name list
		title = f.parent.find("span", {"class": "ListTitle"}).text.strip()

		## Handle Blank Title spot
		if(not title):
			title = "Professor"
		if(len(name) == 2):
			## only first and last
			row.append(no_mi)
		row.extend(name[1:]) ## first and mi
		row.append(name[0]) ## last name

		row.extend([title, DEPT])
		print row
		writer.writerow(row)