#A four-digit integer is given. Find the number of odd digits in it.
number=1233
#Create a variable "var_int" and assign it a four-digit integer value.
a=(number%10)%2
b=((number%100)//10%2)
c=((number%1000)//100%2)
d=number//1000%2
#Print the number of odd digits in the variable "var_int".
print (a+b+c+d)