
pp;o9
# QN5
# Define a function which can generate a list where the 
# values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.

lista=[]
for x in range(1,20):
    x=x**2
    lista.append(x)
print(lista[0:5])