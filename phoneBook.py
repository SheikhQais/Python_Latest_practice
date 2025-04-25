phoneBook = {
    'qais': '03216737482',
    'usman': '03214545069',
    'habib': '03454545670'
}

phoneBook.update({'junaid':'03232345670'})
phoneBook.pop('usman')
for x,y in phoneBook.items():
    print(f"{x.title()} : {y}")
    
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1