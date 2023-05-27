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
# show extensions and how many of each file will be in each directory
#
# confirm organization
#
# complete organization
###

# Functions TODO: break current code into functions
def OrganizeDirByName(directoryPath):
    directoryFileNames = os.listdir(directoryPath)
    print(f"non sorted: {directoryFileNames}")
    return sorted(directoryFileNames)



directoryInput = ""

# Check for command line arguments
args = sys.argv
if len(args) > 1:
    directoryInput = args[1]
    print(f"Running Directory Organizer with argument {directoryInput}")


# verify directoryInput
if directoryInput == None or "":
    print("No directory given.")
elif str.lower(directoryInput) == "this":
    directoryInput = os.getcwd()

while(os.path.isdir(directoryInput) == False):
    print("Please enter a valid directory to organize")
    directoryInput = input("What is the path of the directory you would like to organize?\n" +
                           "Please enter 'this' for current directory or 'exit' to exit program\n")
    if str.lower(directoryInput) == "this":
        directoryInput = os.getcwd()
    elif str.lower(directoryInput) == "exit":
        print("Exiting Directory Organizer...")
        sys.exit()


# Stating directory to organize
directoryName = os.path.basename(directoryInput)
print(f"Organizing {directoryName}")

# confirm directory to organize
input("Press Enter to continue...")


# Preview organization
# get each file extentions and how many of each
print("There will be numberOfUniqueExtensions folders")
# list unique extensions and their count



# Confirm organization




# Organize


input("Press Enter to continue...")








