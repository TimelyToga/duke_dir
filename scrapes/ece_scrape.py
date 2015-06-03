from bs4 import BeautifulSoup as bs
import csv

in_file = "ece_fac_list.html"
out_file = "ece.csv"

DEPT = "ECE"
no_mi = "-"

with open(in_file, 'r') as html_doc:
	soup = bs(html_doc)

names = soup.findAll("div", { "class" : "views-field-title"})

with open(out_file, 'w+') as out:
	writer = csv.writer(out, delimiter="\t")
	for f in names:
		row = []
		name = f.text.strip().split(" ")
		title = f.parent.find("div", {"class": "views-field-field-faculty-title-value"}).span.text.strip()

		## Handle Blank Title spot
		if(title == "" or title == " "):
			title = "Professor"
		row.append(name[0])
		if(len(name) == 2):
			## only first and last
			row.append(no_mi)
		row.extend(name[1:])
		row.extend([title, DEPT])
		print row
		writer.writerow(row)