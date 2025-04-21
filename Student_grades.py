grades = {
  "Ali": 85,
  "Zara": 92,
  "Ahmed": 78,
  "Noor": 88
}

grades["Ahmed"] = 82

grades.update({'Hassan':90})

for x,y in grades.items():
    print(x,"scored",y)