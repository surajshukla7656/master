limport pdb

#debugging is the process of finding and resolving defects or problems within a computer 
#program that prevent correct operation of computer software or a system
pdb.set_trace()
while True:
    try:                        
        age=int(input("enter your age:"))
    except ValueError:                      #executed when error occur
        print("invalid input")
    except:
        print("unexcepted error")
    else:                          #for appending extra code to try when error does not raise
        print("surajshukla")     
    finally:                        #always runs although there is a exception
        break

#----------------- custom exception ---------------->
class NameTooShortError(valueError):
      pass
#code 

# l- line where the program debugger stopped
# n- to execute that line and go to next line
# c- to continue whole code