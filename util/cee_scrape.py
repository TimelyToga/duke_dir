from bs4 import BeautifulSoup as bs
import csv

in_file = "cee_fac_list.html"
out_file = "cee.csv"

DEPT = "CEE"
no_mi = "-"

with open(in_file, 'r') as html_doc:
	soup = bs(html_doc)

faculty = soup.findAll("div", { "class" : "views-row"})

with open(out_file, 'w') as out:
	writer = csv.writer(out_file, delimiter="\t")
	for f in faculty:
		row = []
		name = f.find("div", {"class": "views-field-title"}).span.text.strip().split(" ")
		title = f.find("div", {"class": "views-field-field-faculty-title-value"}).span.text.strip()

		## Handle Blank Title spot
		if(title == "" or title == " "):
			title = "Professor"
		row.append(name[0])
		if(len(name) == 2):
			## only first and last
			row.append(no_mi)
		row.extend([name[1:])
		row.extend([title, DEPT])
		print row
		writer.writerow(row)