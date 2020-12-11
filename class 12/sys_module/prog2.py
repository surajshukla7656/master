import sys
def main(arg):
    print(arg)

main(sys.argv[1])
main(sys.argv[0])

for i in range(len(sys.argv)):
    if i == 0:
        print ("Function name: %s" % sys.argv[0])
    else:
        print ("%d. argument: %s" % (i,sys.argv[i]))

  
  