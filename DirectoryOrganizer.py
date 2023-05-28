import os
import sys



# Functions
def readCommandLineArguments():
    args = sys.argv
    if len(args) > 1:
        arg = args[1]
        print(f"Running Directory Organizer with argument {arg}")
        return arg
    else:
        return ""

def verifyDirectoryInput(directory):
    if(directory == None or ""):
        print("No directory given.")
        return 
    elif str.lower(directory) == "this":
        return True
    elif str.lower(directory) == "exit":
        print("Exiting Directory Organizer...")
        sys.exit()
    elif os.path.isdir(directory):
        return True
    else:
        return False

def OrganizeDirectoryIntoDictionary(directoryPath, fileNamesList):
    subDirectories = {}
    for fileName in fileNamesList:
        extensionSubDirectoryName = os.path.splitext(fileName)[1][1:]
        if extensionSubDirectoryName in subDirectories:
            subDirectories[extensionSubDirectoryName].append(fileName)
        else:
           subDirectories[extensionSubDirectoryName] = [fileName]
    return subDirectories

def displayOrganizationPreview(subDirectoriesDictionary):
    print("Organization Preview:\n" +
          f"There will be {len(subDirectoriesDictionary)} new subdirectories in this directory\n")
    for key in subDirectoriesDictionary:
        print(f"{key} will contain {len(subDirectoriesDictionary[key])} files")

def moveFilesToSubdirectories(directoryPath, fileNamesList):
    directoryAbsolutePath = os.path.abspath(directoryPath)
    for subDirectory in subDirectoriesDictionary:
        os.mkdir(subDirectory)   ## makes directory correctly
        for fileName in subDirectoriesDictionary[subDirectory]:
            oldFilePath = os.path.join(directoryAbsolutePath, fileName)  ## cannot find path
            newFilePath = os.path.join(directoryAbsolutePath, subDirectory, fileName)
            os.replace(oldFilePath, newFilePath)
            #TestDirectory



# main
directoryInput = readCommandLineArguments()


    ## Verify directory input
while(not verifyDirectoryInput(directoryInput)):
    print("Please enter a valid directory to organize")
    directoryInput = input("What is the path of the directory you would like to organize?\n" +
                           "Please enter 'this' for current directory or 'exit' to exit program\n")
    
if str.lower(directoryInput) != "this":
    os.chdir(directoryInput)

directory = os.getcwd()

    ## Get directory name and list of files in directory
directoryName = os.path.basename(directory)
fileNames = os.listdir(directory)

print(f"Organizing {directoryName}")
subDirectoriesDictionary = OrganizeDirectoryIntoDictionary(directory, fileNames)
displayOrganizationPreview(subDirectoriesDictionary)


    ## finalize organization
confirm = input("Confirm organization? (y/n)\n")
while str.lower(confirm) != "y" and str.lower(confirm) != "n":
    confirm = input("Please enter 'y' to confirm organization or 'n' to cancel the organization.\n")

if str.lower(confirm) == "y":
    moveFilesToSubdirectories(directory, fileNames)
    print(f"{directoryName} has been organized\nExiting Directory Organizer...")
else:
    print("Organization cancelled\nExiting Directory Organizer...")
    sys.exit()