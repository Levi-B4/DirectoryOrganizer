import os
import sys

###
#                   outline
#
# make program accept parameter of directory to organize
#
# if no path given
#   What is the path of the directory you would like to organize?
#
# How do you want to organize it?
# [fileName, fileType, fileSize, fileCreationDate]
#
# open directory
# is this how it should be organized? if not restart program at point of how do you want to organize it, if yes then exit program
###

directoryInput = ""

# Check for command line arguments
args = sys.argv
if len(args) > 1:
    directoryInput = args[1]
    print(f"Running Directory Organizer with argument {directoryInput}")


#verify directoryInput
if directoryInput == None or "":
    print("No directory given.")
elif str.lower(directoryInput) == "this":
    directoryInput = os.getcwd()

while(os.path.isdir(directoryInput) == False):
    print("Please enter a valid directory to organize")
    directoryInput = input("What is the path of the directory you would like to organize? (enter 'this' for current directory or 'exit' to exit program)")
    if str.lower(directoryInput) == "this":
        directoryInput = os.getcwd()
    elif str.lower(directoryInput) == "exit":
        print("Exiting Directory Organizer...")
        sys.exit()


#Stating directory to organize
directoryName = os.path.dirname(directoryInput)
print(f"Organizing {directoryName}")

input("Press Enter to continue...")

#List files in directory
directoryFiles = os.listdir(directoryInput)
print(directoryFiles)

input("Press Enter to continue...")