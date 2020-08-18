from sys import argv
from os.path import exists

script, file_name = argv

if exists(file_name):
    opened_file = open(file_name, 'r+')

for line in opened_file:
    opened_file.write(line)
