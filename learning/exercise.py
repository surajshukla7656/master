from csv import writer

with open("csvfile","w") as f:
    csv_writer=writer(f)
    csv_writer.writerow(["name","age"])
    csv_writer.writerow(["suraj",17])

with open("csvfile1","w") as f:
    writer(f).writerows([["name","age"],["suraj","17"],["kuldeep",14]])

from csv import DictWriter
with open("csvfile2","w") as f:
    csv_writer=DictWriter(f,fieldnames=["name","age"])
    csv_writer.writeheader()
    csv_writer.writerows([
        {"name":"surajshukla",
        "age":17},
        {"name":"abhay mishra",
        "age":12
        }
])

from csv import reader
with open("csvfile","r") as f:
    csv_reader=reader(f)
    for line in csv_reader:
        print(line)

from csv import DictReader
with open("csvfile2","r") as f:
    csv_reader=DictReader(f)
    print(csv_reader.__dict__)
    for i in csv_reader:
        print(i)

