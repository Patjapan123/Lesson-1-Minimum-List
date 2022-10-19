def min(list):
    miles=list[0]
    for i in range(len(list)):
        if list[i] < miles:
            miles=list[i]
    return miles

first= [45,44,43,23]
second= [44,33,22]

print("Minimum value:", min(first))
print("Minimum value:", min(second))

