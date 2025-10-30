with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

calculation = open('calculation.txt', 'w')
calculation.write("This is a new file created for calculations.\n")
calculation.write("It will store the results of various calculations.\n")
calculation.close()

with open('calculation.txt', 'r') as calculation:
    print(calculation.readlines())


with open('calculation.txt', 'a') as calculation:
    calculation.write("Appending a new line to the existing file.\n")

print("After appending:")
with open('calculation.txt', 'r') as calculation:
        for x in calculation:
            print(x)