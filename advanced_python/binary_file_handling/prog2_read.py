import pickle

# with open('/home/surajshukla7656/Documents/Python/nextpython/advanced_python/binary_file_handling/binaryFile','rb') as f:

#     try:
    
#         while True:

#             a=pickle.load(f)

#             print(a)

#     except:
#         print('done')

with open('/home/surajshukla7656/Documents/Python/nextpython/advanced_python/binary_file_handling/binaryFile','rb') as f :
    
    a=pickle.load(f)

    print(a)

    