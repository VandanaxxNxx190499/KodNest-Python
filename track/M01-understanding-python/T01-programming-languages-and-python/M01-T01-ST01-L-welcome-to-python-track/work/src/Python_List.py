values = list(map(int, input().split()))
print("Original: ",values)
values.append(50) #adds value at the end
print("Append: ",values)
values.insert(2, 60)
print("Insert: (2,60)",values)
values.remove(10) # remove by value
print("remove by value", values)
values.pop() #remove last element
print("pop", values)
del values[1] # remove ny index
print("del by index:", values) 
