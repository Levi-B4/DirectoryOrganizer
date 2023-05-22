import os

#make program accept paramerter of directory to organize

#if no path given
#What is the path of the directory you would like to organize?

#How do you want to organize it?
#[fileName, fileType, fileSize, fileCreationDate]

#open directory
#is this how it should be organized? if not restart program at point of how do you want to organize it, if yes then exit program

directoryInput = input("What is the path of the directory you would like to organize? (enter 'this' for current directory)")


if directoryInput == "this":
    directory = os.getcwd()
else:
    directory = directoryInput #add error handling for invalid directory

directoryFileList = os.listdir(directory)

print(directoryFileList)

input("Press Enter to continue...")