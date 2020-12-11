import pickle


def write_data():
    
    try:
        while True:

            with open('/home/surajshukla7656/Documents/Python/nextpython/advanced_python/binary_file_handling/binaryFile','ab') as f:

                name=input('Enter name : ')
                
                if name=='':
                    break

                pickle.dump(name,f)

    except:
        print()
write_data()
