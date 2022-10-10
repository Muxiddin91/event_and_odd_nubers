#A four-digit integer is given. Find the sum of even digits in it.
n=8475
x1=n%10
n=n//10
x2=n%10
n=n//10
x3=n%10
n=n//10
x4=n%10
print(x1,x2,x3,x4)
s=0
s=s+(x1+1)%2*x1
s=s+(x2+1)%2*x2
s=s+(x3+1)%2*x3
s=s+(x4+1)%2*x4
print(s)
#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".