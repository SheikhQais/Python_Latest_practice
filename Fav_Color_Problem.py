my_colors = ['red', 'blue', 'green', 'yellow']
friend_colors = ['blue', 'black', 'green', 'white']

my_colors = set(my_colors)
friend_colors = set(friend_colors)

Common_color = my_colors.intersection(friend_colors)
print("common colors:",Common_color)

Colors_only = my_colors.difference(friend_colors)
print("Colors only I like:",Colors_only)

Union_colors = my_colors.union(friend_colors)
print("Combined colors:",Union_colors)