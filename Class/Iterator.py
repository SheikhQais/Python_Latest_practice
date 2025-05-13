# myTuple = ('bnana','apple','orange','Mango')
# myIter = iter(myTuple)
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))

# #Even that strings are iterator
# mystr = "banana"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

class myClass:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
cls = myClass()
myiter = iter(cls)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))