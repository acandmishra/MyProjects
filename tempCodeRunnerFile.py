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