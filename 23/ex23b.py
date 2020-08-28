from sys import argv

script, file_name = argv
file = open(file_name)

print(file.read())

# don't forget to close a file
file.close()
