from bs4 import BeautifulSoup as bs
import csv

in_file = "bme_fac_list.html"
out_file = "dept_list.txt"
DEPT = "BME"

with open(in_file, 'rw') as html_doc:
	soup = bs(html_doc)

faculty = soup.findAll("div", { "class" : "views-row"})

with open(out_file, 'w') as out:
	for f in faculty:
		name = f.find("div", {"class": "views-field-title"}).span.text.strip().split(" ")
		title = f.find("div", {"class": "views-field-field-faculty-title-value"}).span.text.strip()
		if(title == "" or title == " "):
			title = "Professor"
		if(len(name) == 2):
			## only first and last
			print "%s	-	%s	%s	%s" % (name[0], name[1], title, DEPT)
		else:
			## + at least one middle initial
			print "%s	%s 	%s 	%s	%s" % (name[0], name[1], name[2], title, DEPT)
