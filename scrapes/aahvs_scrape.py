from bs4 import BeautifulSoup as bs
import csv

dept = "aahvs"

in_file = "htmls/" + dept + "_fac_list.html"
out_file = "depts/" + dept + ".tsv"

DEPT = dept.upper()
no_mi = "-"

with open(in_file, 'r') as html_doc:
	soup = bs(html_doc)

faculty = soup.findAll("div", { "class" : "views-field views-field-title"})

with open(out_file, 'w+') as out:
	writer = csv.writer(out, delimiter="\t")
	for f in faculty:
		row = []
		name = f.h4.a.text.strip().split(" ")
		title = f.parent.find("div", {"class" : "views-field views-field-field-fds-job-title"}).h5.text.strip()

		## Handle Blank Title spot
		if(not title):
			title = "Professor"
		row.append(name[0])
		if(len(name) == 2):
			## only first and last
			row.append(no_mi)
		row.extend(name[1:])
		row.extend([title, DEPT])
		print row
		writer.writerow(row)