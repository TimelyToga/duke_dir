from bs4 import BeautifulSoup as bs
import csv

dept = "pe"

in_file = "htmls/" + dept + "_fac_list.html"
out_file = "depts/" + dept + ".tsv"

DEPT = dept.upper()
no_mi = "-"

with open(in_file, 'r') as html_doc:
	soup = bs(html_doc)

rows = soup.findAll("tr")

with open(out_file, 'w+') as out:
	writer = csv.writer(out, delimiter="\t")
	for f in rows:
		items = f.findAll("td")
		row = []
		name = items[0].text.strip().split(" ")#f.text.strip().split(" ") ## returns itemized name list
		title = items[1].text.strip()#f.parent.findAll("li", {"class": "title"})[0].text.strip()

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