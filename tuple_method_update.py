colors = ('red', 'blue', 'green', 'yellow')
print(colors.count('blue'), 'times blue appears in tuple')

TuL = list(colors) #Converting Tuple into List to make changes As Tuple is unchangeable or immutable
TuL.append('purple')

colors = tuple(TuL) #Converting List back to Tuple
print("Here is the updated tuple colors: ", colors)