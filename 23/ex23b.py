from sys import argv

script, file_name = argv
file = open(file_name)

print(file.read())

file.close()
