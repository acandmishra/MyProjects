path = "D:\Computer Practice\Programming\days.txt"
myfile=open(path,"r")
print("file opened")
# print(myfile.read()) # will read the whole file till end
# print(myfile.read(6)) # read the strings till given no of bytes
# print(myfile.readline()) # read the text file line by line (a line at a time)
# print(myfile.readlines()) # return a list with each element being a line from the file
# myfile.write("""
# hello ! good morning
# python is a very awesome language 
# lets unite together and learn this awesome amazing next level language""")
print(myfile.read())
myfile.close()
print("file closed")
