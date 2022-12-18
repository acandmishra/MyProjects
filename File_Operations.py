from collections import Counter
path1=r"D:\Computer Practice\Programming\text1.txt"
path2=r"D:\Computer Practice\Programming\text2.txt"
f1=open(path1,"r+")
print("opened file 1")
f2=open(path2,"r+")
print("opened file 2")
print("\nREADING FILE 1.....\n")
print(f1.read())
print("\nREADING FILE 2.....\n")
print(f2.read())
f1.seek(0)#going back to 0th place
f2.seek(0)#going back to 0th place
print("\ntotal number of lines in file 1:",len(f1.readlines()))
print("total number of lines in file 2:",len(f2.readlines()))
f1.seek(0)
f2.seek(0)
print("opened file 3")
f3 = open("f1+f2.txt","r+")
f3.write(f1.read()+f2.read()) #contents transfered in file 3
f3.seek(0)
W = f3.read().split()
C = Counter(W)
print(C.most_common(1))

f1.close()
f2.close()
f3.close()