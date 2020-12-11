import pickle

def createFile():
    fobj = open("Book.dat","ab")
    BookNo = int(input("Book Number : "))
    Book_Name = input("Name :")
    Author = input("Author: ")
    Price = int(input("Price : "))
    record = [BookNo, Book_Name, Author, Price]
    pickle.dump(record,fobj)
    fobj.close()

def CountRec(Author):
    fobj = open("Book.dat","rb")
    num = 0
    try:
        while True:
            record = pickle.load(fobj)
            if Author == record[2]:
                num = num + 1
    except:
        fobj.close()
    return num

createFile()   
createFile()

print(CountRec("Prem Chand"))

import pickle

def createFile():
    fobj = open('STUDENT.DAT', 'ab')
    admission_no = int(input("Admission Number: "))
    name = input("Name: ")
    perc = float(input("Percentage marks: "))
    rec = [admission_no, name, perc]
    pickle.dump(rec, fobj)
    fobj.close()

def CountRec():
    fobj = open("STUDENT.DAT","rb")
    num = 0
    try:
        while True:
            rec = pickle.load(fobj)
            if rec[2] > 75:
                print(rec[0],rec[1],rec[2],sep="\t")
                num = num + 1
    except:
        fobj.close()
    return num

createFile()
createFile()
createFile()
