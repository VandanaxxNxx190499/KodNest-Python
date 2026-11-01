values = list(map(int, input("Enter the values : ").split()))
# Slicing

print(values[1:4]) # start at index 1 to index 4-1
print(values[:3]) # index 0 to 3-1
print(values[2:]) # start from index 2 to all
print(values[::-1]) # reverse the list
print(values[:]) # prints all values

#List in built functions
print(len(values))
print(sum(values))
print(max(values))
print(min(values))
print(sorted(values))
values.sort()
print(values)
values.reverse()
print(values)
print(values.count(10))
print(values.index(20))

# Enter the values : 20 40 50 6 7 8 1 2 3 4
# [40, 50, 6]
# [20, 40, 50]
# [50, 6, 7, 8, 1, 2, 3, 4]
# [4, 3, 2, 1, 8, 7, 6, 50, 40, 20]
# [20, 40, 50, 6, 7, 8, 1, 2, 3, 4]
# 10
# 141
# 50
# 1
# [1, 2, 3, 4, 6, 7, 8, 20, 40, 50]
# [1, 2, 3, 4, 6, 7, 8, 20, 40, 50]
# [50, 40, 20, 8, 7, 6, 4, 3, 2, 1]
# 0
# 2

# Operation Typical - time complexity
# Access by index	O(1)
# Update by index	O(1)
# Traversal	O(n)
# Search (unsorted)	O(n)
# Append	O(1) amortised
# Insert at beginning	O(n)
# Delete at beginning	O(n)
# Pop from end	O(1)
# Sorting	O(n log n)