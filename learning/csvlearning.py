#csv - comma separated values - used to store tabular data

from csv import reader 
with open("csvfile","r") as f:
    csvreader=reader(f) #an iterator containing lines of csvfile as element
    print(csvreader)
#reading csv file through dictReader
from csv import DictReader
with open("csvfile","r") as f:
    csv_reader=DictReader(f,delimiter="|") #creates ordered dictionary 
    for row in csv_reader:
        print(row["email"])

#writing in csv file
from csv import writer
with open("file.txt","w") as f:
    csv_writer=writer(f)
    #methods - writerow ,writerows
    csv_writer.writerow(["name","country"])
    csv_writer.writerow(["suraj","india"])

    csv_writer.writerows([["name","country"],["surajshukla","india"]])

#writing in csv using dictwriter

from csv import DictWriter
with open("csvfile2","w") as f:
    csv_writer=DictWriter(f,fieldnames=["firstname","lastname","age"])
    csv_writer.writeheader()
    csv_writer.writerow({
        "firstname":"surajsingh",
        "lastname":"singh",
        "age":34
    })

    csv_writer.writerows([
    {'firstname':"kuldeep","lastname":"shukla","age":43},
    {"firstname":"abhay","lastname":"mishra","age":3}
    ])

#read and write in csvfile
from csv import DictWriter,DictReader
with open("csvfile","r") as rf:
    with open("csvfile2","w") as wf:
        csv_reader=DictReader(rf)
        csv_writer=DictWriter(wf,fieldnames=["firstname","lastname","age"])
        csv_writer.writeheader()
        for row in csv_reader:
            fname,lname,age=row["firstname"],row["lastname"],row["age"]
            csv_writer.writerow({
                "firstname":fname.upper(),
                "lastname":lname.upper(),
                "age":age
            })
 
 