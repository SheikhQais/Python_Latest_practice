li = [2, 3, 2, 4, 3]
for i in range(len(li) + 1):
    for j in range(len(li)+ 1):
        if li[i] == li[j]:
            li.remove(li[j])
print(li)