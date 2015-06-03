from bs4 import BeautifulSoup as bs



with open('trinity_dept_list.html', 'rw') as html_doc:
	soup = bs(html_doc)

depts = soup.findAll("td", { "class" : "views-field views-field-title"})

with open('dept_list.txt', 'w') as out:
	for d in depts:
		print d.strong.text