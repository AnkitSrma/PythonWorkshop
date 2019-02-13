
import os


# function to search the files with user given extension
def searchInDir (extension):
    #path = "D:\DWIT\sem 5\SM\python\Lab\Ankit"

    path = input("Enter the path of directory to search: ")
    files = os.listdir(path)

    file = list()
    for each in files:
        if each.endswith(extension):
            file.append(each) #adds each file with the extension in the list

    return file




# asking for extension with users
extension = input("Enter the extension of the file: ")


files = searchInDir(extension)
for each in files:
    print(each)



