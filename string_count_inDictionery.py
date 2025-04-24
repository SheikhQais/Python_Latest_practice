_str = input('Enter your sentence:')
dic = {}
words = _str.split()
for x in words:
    count = words.count(x)
    dic.update({x:count})
    
print(dic)