import math

x = math.sqrt(64)

print(x)

# f = open('D:/Python_Latest_practice/Class/myfile.txt', 'a')
# content  = f.read()
# print(content)

# f.append('Occupation: Software Developer')
# print(f.read())
# f.close()

# Step 1: Read the file line-by-line and print each line
# with open('D:/Python_Latest_practice/Class/myfile.txt') as f:
#     for x in f:
#         print(x)

with open('D:/Python_Latest_practice/Class/myfile.txt', 'r') as f:
    content = f.read()

update_content = content.replace('City: New York', 'City: San Francisco')

# Step 2: Check if the line already exists, and only append if it's not there
if 'Occupation: Software Developer' not in content:
    with open('D:/Python_Latest_practice/Class/myfile.txt', 'a') as f:
        f.write('\nOccupation: Software Developer')

# Step 3: Read and writing updated file content to the file content
with open('D:/Python_Latest_practice/Class/myfile.txt', 'w') as f:
    f.write(update_content)

# Step 4: Read and print the entire file content    
with open('D:/Python_Latest_practice/Class/myfile.txt') as f:
    print(f.read())