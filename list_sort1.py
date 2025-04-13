list_ = [4,5, 6, 5,6,3,7,8 ,9]
unique = [] # declaring new list for sorting
i =0 # initializing variable for control of loop flow
print("list after sorting and square of items is:")
print(list_)
while i < len(list_):
    if list_[i] not in unique:
        unique.append(list_[i])
    i += 1
for i in range(len(unique)):
    unique[i] = unique[i]**2
unique.sort()
print("New sorted list with square of items is:")
print(unique)