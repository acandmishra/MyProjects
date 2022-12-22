course = "python for beginners"
print(len(course))    
print(f'''{course.lower()} 
{course.upper()}
{course.find("o")} 
{course.replace("python","computer")}
{"beginners" in course}
{course.title()}
{course.capitalize()}''')
# String Functions Used:-
# length function
# lower case
# upper case
# find |it gives the index where the passed substring is found or starting index when multiple characters are passed
# replace 
# in
# title (it will return each word with capital first letter)
# capitalize
a="hello"
b="Hello"
print(a==b)
print(a.casefold()==b.casefold()) # casefold will let us ignore the case of characters and compare the character value
print(a.center(40,"*")) # centres the string with passed character surrounding it // chr is optional 
print(a.rjust(10,"*")) # right justify the string with passed character // chr is optional
print(a.ljust(10,"*")) # left justify the string with passed character // chr is optional
c="my name is acand mishra"
print(c.count("a"))
print(c.count("a",3,9)) #takes three arg, 1.string to be counted, 2.strat index, 3.end index
#by default above takes whole string 
print(c.endswith("a")) #gives boolean
# print(c.index("i"))
# index works same as find except it gives error when not found whereas find returns -1
x="set\n"
print(a.isidentifier()) # it tellswhether the passed string can be used a variable name or not
#other functions are
# isalnum()
# isalpha()
# isdigit()
# islower()
# isupper()
# swapcase() | to swap U to L and L to U
print(x.isprintable()) # gives false as a has escape sequence character
z=" "
print(z.isspace()) # gives true as z has only space
p="The Times Of India"
print(p.istitle()) # gives true if the string is title cased

w="abababac123ababbba"
print(w.lstrip("a")) # this will remove a from left side 
print(w.lstrip("ab")) #this will remove all the continuous a and b until different char appears , here until c
# rstrip will do the same from right side
# strip will do the same from both the sides

print(p.split()) # gives list with separate words
# when nothing is passed in split then space is taken by default
print(a:="123".split())
# print(l.splitlines()) gives list with each lines as an element
num="766606387"
print(num.zfill(10)) # adds number to the front until the length is 10
part="Germany"
print(part.partition("m")) # will do 3 partitions always and gives a tuple with passed substring as centre part
#if substring is not passed then the whole string is kept on first part and 2nd and 3rd are empty
print(part.partition("w"))