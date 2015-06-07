from bs4 import BeautifulSoup as bs
import csv

dept = "div"

in_file = "htmls/" + dept + "_fac_list.html"
out_file = "depts/" + dept + ".tsv"

DEPT = dept.upper()
no_mi = "-"

with open(in_file, 'r') as html_doc:
	soup = bs(html_doc)

names = soup.findAll("div", { "class" : "views-field views-field-nothing"})

with open(out_file, 'w+') as out:
	writer = csv.writer(out, delimiter="\t")
	for f in names:
		row = []
		name = f.span.a.text.strip().split(" ") ## returns itemized name list
		title = f.parent.findAll("div", {"class": "views-field views-field-field-person-position"})[0].div.text.strip()

		## Handle Blank Title spot
		if(not title):
			title = "Professor"
		row.append(name[0]) ## last name
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
		writer.writerow(row)