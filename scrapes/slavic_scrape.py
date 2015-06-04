from bs4 import BeautifulSoup as bs
import csv

dept = "slavic"

in_file = "htmls/" + dept + "_fac_list.html"
out_file = "depts/" + dept + ".tsv"

DEPT = dept.upper()
no_mi = "-"

with open(in_file, 'r') as html_doc:
	soup = bs(html_doc)

names = soup.findAll("li", { "class" : "name"})

with open(out_file, 'w+') as out:
	writer = csv.writer(out, delimiter="\t")
	for f in names:
		row = []
		name = f.text.strip() ## returns itemized name list
		title = f.parent.findAll("li", {"class": "title"})[0].text.strip()

		name = name.split(", ") ## 0 = last, 1 = first MI
		fmi = name[1].split(" ") ## 0 = f, 1 = mi
		## Handle Blank Title spot
		if(not title):
			title = "Professor"
		row.append(fmi[0]) ## last name
		if(len(fmi) == 1):
			## only first and last
			row.append(no_mi)
		row.append(name[0]) ## last name

		row.extend([title, DEPT])
		print row
		writer.writerow(row)