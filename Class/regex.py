import re

def email_validate(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    if re.match(pattern, email):
        print("Valid Email")
    else:
        print("In-Valid Email")
        
email_validate("test@example.com")
email_validate("invalid-email@com")
email_validate("user@.com")

def extract_phone_numbers(txt):
    patt = r'\d{3}-\d{3}-\d{4}'
    number = re.findall(patt,txt)
    return number

txt = "Contact us at 123-456-7890 or 987-654-3210. Office: 111-222-3333."
print(extract_phone_numbers(txt))