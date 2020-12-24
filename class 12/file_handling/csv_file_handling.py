import csv      # Line 1
def addCsvFile(UserName,PassWord):
    f = open('user.csv','a') # to write / add data into the CSV file
                            # Line 2
 
    newFileWriter = csv.writer(f)
    newFileWriter.writerow([UserName,PassWord])
    f.close()

#csv file reading code
def readCsvFile():
    with open('user.csv','r') as newFile:  # to read data from CSV file
        newFileReader = csv.reader(newFile) # Line 3

        for row in newFileReader:
            print (row[0],row[1])
        newFile.close() # Line 4

addCsvFile('Arjun','123@456')
addCsvFile('Arunima','aru@nima')
addCsvFile('Frieda','myname@FRD')
readCsvFile()   #Line 5


import csv

with open('people.csv', 'r') as file:
    content = csv.reader(file)
    for row in content:
        print(row)

import csv
with open('people2.csv', 'r') as file:
    content = csv.reader(file, delimiter='\t')
    for row in content:
        print(row)


with open('protagonist.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])

import csv
with open('protagonist2.csv', 'w') as file:
    writer = csv.writer(file, delimiter = '\t')
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])