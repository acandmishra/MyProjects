import re
a="hello every one how are you all doing in 21st century year 2022"
print(re.findall(r"\d",a))
print(re.findall(r"\d+",a))
print(re.findall(r"\D",a))
print(re.findall(r"\D+",a))
print(re.findall(r"\s",a))
print(re.findall(r"\S",a))
print(re.findall(r"\w",a))
print(re.findall(r"\W",a))