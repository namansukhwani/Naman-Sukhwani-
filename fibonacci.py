a=int(input("Enter a no for fibonacci series till there : "))
term=0
t1=0
t2=1
print("Fibonacci series : \n")
print(t1)
print(t2)
term=t1+t2
while term<a :
    print(term," ")
    t1=t2
    t2=term
    term=t1+t2
    
