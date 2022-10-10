#A four-digit integer is given. Find the number of even digits in it.
var_int=2223
a=(var_int%10)%2
b=((var_int%100)//10%2)
c=((var_int%1000)//100%2)
d=(var_int//1000)%2
#Create a variable "var_int" and assign it a four-digit integer value.
a1=4-(a+b+c+d)
#Print the number of even digits in the variable "var_int".
print(a1)