contacts = {
  "Ali": {"phone": "12345", "email": "ali@example.com"},
  "Zara": {"phone": "67890", "email": "zara@example.com"}
}

contacts.update({'Ahmad':{"phone": "12349", "email": "ahmad@example.com"}})
contacts["Zara"]["phone"] = "090078601"

for x, obj in contacts.items():
    print(x)
    print('phone',obj['phone'])
    print('email',obj["email"])
    
    