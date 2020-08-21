import os
print(os.getcwd())       # to check the current working directory

# #-------------------------to create a new folder------------------------->>>

# #os.mkdir("foldername")     # to create a new folder

# print(os.path.exists("foldername"))

# if os.path.exists("foldername"):
#     print("already exists ")

# else:
#     os.mkdir("foldername")

# #------------------------to create a new file------------------------------>>>
# open("file.txt","a").close()

# #------------------to move into another directory--------------------------->>
 
# #os.chdir("<directory") # to go into a new  working directory 

# # ---------------to 
# print(os.listdir())
# for item in os.listdir():
#     path=os.path.join(os.getcwd(),item)
#     print(path)


#------------------------to check all data about a directory--------------->>
import os
os.chdir("/home/surajshukla2703/Documents/pythonprogs/learning")
fileiter=os.walk("/home/surajshukla2703/Documents/pythonprogs/learning")
for current_path,folder_names,file_names in fileiter:
    print(f"current path:{current_path}")
    print(f"folder names :{folder_names}")
    print(f"file names : {file_names}")

#------------------------------------------
#os.rmdir("<folder>") #deletes empty folder

os.makedirs("new/movies")
import shutil
shutil.rmtree("<folder>") #deletes pemanently

shutil.copytree("folder_path","new_path/new_name") #for copy file in different location

shutil.copy("file.txt","documents/file.txt")

shutil.move("file.txt","documents/file2.txt")