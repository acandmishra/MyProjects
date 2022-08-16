try:
    a=int(input("age:"))
    income=20000
    risk= income/a
    print(a)  
except ZeroDivisionError:
    print("age can not be zero!!")#to deal with zero divison error
except ValueError:#this is used to handle errors which occur when we convert non numeric value to numeric
    print("invalid value!!")