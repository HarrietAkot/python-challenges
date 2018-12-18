
marks = [23,4,5,6,64,90,67,98,45,23,67,78,89]

list1 = []
list2 =[]


for x in marks:
    if x >50:
        list1.append(x)
    else:
        list2.append(x)
print(f"List 1 has {list1}")
print(f"List 1 has {list2}")
for a in marks:
    if a > 90 and a < 100:
        print(a, 'is excellent')
    elif a > 70 and a <= 89:
        print(a, 'is very good')
    elif a > 60 and a < 69:
        print(a, 'is good')
    elif a > 40 and a < 59:
        print(a, 'is poor')
    elif a > 20 and a < 39:
        print(a, 'is very poor')
    else:
        print(a, 'repeat')