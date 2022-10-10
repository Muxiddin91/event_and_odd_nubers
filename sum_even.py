#A four-digit integer is given. Find the sum of even digits in it.
number=1234
a=number%10
b=(number%100)//10
c=(number%1000)//100
d=number//1000
jami=a+b+c+d
#Create a variable "var_int" and assign it a four-digit integer value.
var_int=9826
a1=(var_int%10)
b1=(var_int%100)//10
c1=(var_int%1000)//100
d1=var_int//1000
a2=(a1+1)%2
b2=(b1+1)%2
c2=(c1+1)%2
d2=(d1+1)%2
print (a2, b2, c2, d2)
#Create a variable "sum_even" and assign it 0.
sum_just=a1*a2+b1*b2+c1*c2+d1*d2
print(sum_just)
#Find the sum of the even digits in the variable "var_int".