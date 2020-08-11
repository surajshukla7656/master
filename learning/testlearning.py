# import os 

# print(f"you are in directory----------->>>{os.getcwd()}")

# # os.mkdir("surajshukla")

# # print(os.path.exists("surajshukla"))

# if os.path.exists("surajshukla")==True:
#     pass
# else:
#     os.mkdir("surajshukla")

# open("suraj","a").close()

# # os.chdir("surajshukla") 
# # print(os.getcwd())
# print(os.listdir())
# for item in os.listdir():
#     print(os.path.join(os.getcwd(),item))
# for x,y,z in  os.walk(os.getcwd()):
#     print(f"{x}\n{y}\n{z}")

# import os
# os.chdir("/home/surajshukla2703/Documents/pythonprogs/learning")
# fileiter=os.walk("/home/surajshukla2703/Documents/pythonprogs/learning")
# for current_path,folder_names,file_names in fileiter:
#     print(f"current path:{current_path}")
#     print(f"folder names :{folder_names}")
#     print(f"file names : {file_names}")


with open("/home/surajshukla2703/Pictures/Screenshot from 2020-07-03 18-31-57.png","rb") as f:
    a=f.readlines()
    for i in a:
        print(i)