# python program to remove all the lines that contain the character 'a' in a file and write it to another file

import os
import sys

# main
def main(file):

    with open(file,'r') as f   :

        with open(file,'w') as nf :

            for char in f.readlines():

                if 'a' in char:

                    nf.write(char)

                else:
                    with open('temporaryfile','a') as tf:

                        tf.write(char)

    f.close()
    nf.close()

    os.remove(file)
    os.rename('temporaryfile',file)


# driver's code
if __name__=='__main__':

    file=sys.argv[1]

    main(file)