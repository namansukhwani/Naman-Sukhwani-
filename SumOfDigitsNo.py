a=int(input("Enter a no "))
sum=0
while a!=0 :
    sum=sum+a%10
    a=a//10
print("Sum of all digits of the No is ",sum)
