from pathlib import Path
path = Path() # this will take the name of the file to be operated in String form , keeping it empty will start from current file
for files in path.glob("*"):# to get names of all files and directories
    print(files)



# to remove --> rmdir() , to make --> mkdir()
# glob("*.*") to get names of only files , .py for python , .xls for excel files etc...