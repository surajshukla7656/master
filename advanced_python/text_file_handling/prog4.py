with open('nextpython/advanced_python/text_file_handling/basics.txt','w') as f :

    print(f.tell())                                # return position

    print(f.write('My name is surajshukla\ni read in 12 class\nmy am is to be scientist')) 

    print(f.tell())

    print(f.seek(4))                               # position changes to specified position

    print(f.tell())

    print(f.truncate())                            # truncates from the present position

    print(f.truncate(5))                           # truncates from 5 