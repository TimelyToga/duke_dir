import csv
import os.path
import sys

folder = "depts"
slashed_folder = folder + "/"
out_file = "master_faculty.tsv"

with open(out_file, "w+") as out:
	for filename in os.listdir(folder):
		with open(slashed_folder + filename, "r") as cur_file:
			out.writelines(cur_file.readlines())