#Right angled Triangle
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()

#Inverted Right angled Triangle
n=5
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()

#Diamond Pattern
n=5
for i in range(n):
      for j in range(n-i-1):
              print("",end="")
      for  j in range(2*i+1):
        print("*",end="")
print()
for i in range(n-2,-1,-1):
     for j in range(n-i-1):
          print("",end="")
     for j in range(2*i+1):
          print("*",end="")
print()

#Armstrong Number
n=int(input("Enter a number: "))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if n==sum:
    print(n,"is an Armstrong number")

#Hollow Square Pattern
n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

#Pascal's Pattern
n = 5
for i in range(n):
   
    for j in range(n - i - 1):
        print(" ", end="")  
    
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()  

