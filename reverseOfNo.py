a=int(input("enter a no to reverse : "))
rev=0
while a!=0 :
    rim=a%10
    rev=(rev*10)+rim
    a=a//10
print("reverse of the no is ",rev)
