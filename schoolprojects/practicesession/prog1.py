# python program to read a text file line by line 
# and display each word separated by a '#'

def main():
    with open('textfile1.txt','r') as f:
        
        file_content=f.read().split()
        for word in file_content:
            print(word,end='#')

    f.close()


if __name__=='__main__':
    main()
