from bs4 import BeautifulSoup as bs
import requests
import csv

dept = "med"

out_file = "htmls/" + dept + "_fac_list.html"

count = 0
max_page_num = 31

base_url = "http://medicine.duke.edu/faculty?&page=%d"

with open(out_file, 'w+') as out:
	for i in range(0, max_page_num+1):
		cur_url = base_url % i
		response = requests.get(cur_url, verify=False)
		soup = bs(response.text)

		peeps = soup.findAll("div", {"class": "node__content"})
		for p in peeps:
			out.write(p.encode('utf8'))
			count += 1
		print "Done with page %d" % i

print "\n\n\nSuccessfully wrote %d lines to %s\n\n" % (count, out_file)