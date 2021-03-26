# python program to remove all the lines that contain the character a in 
# in a file and write it to another file

import os

def main():

     f1=open('textfile5','r') 
     f2=open('newtextfile5','w')
     f3=open('temtextfile5','w')

     for line in f1.readlines():    
        if 'a' in line or 'A' in line:
            f2.write(line)

        else:
            f3.write(line)

     f1.close()
     f2.close()
     f3.close()
     
     os.remove('textfile5')
     os.rename('temtextfile5','textfile5')
     print('Done')


if __name__=='__main__':

    main()
