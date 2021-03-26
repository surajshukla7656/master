# python program to find most recurring emails/words

def main():
    with open('textfile9','r') as f:

        file_content=f.read().split()
        
        frequency_count={}
        for word in file_content:

            if word in frequency_count:
                frequency_count[word]+=1
            else:
                frequency_count[word]=1

    # searching for max frequency
    max_frequency=max(frequency_count.values())
    print('most recurring word :',end=' ')
    for word,frequency in frequency_count.items():
        if frequency==max_frequency:

            print(word,'-',frequency,end=' ')

    print()

if __name__=='__main__':

    main()
