emp_dir = {
  'E001': {'name': 'Ali', 'dept': 'HR'},
  'E002': {'name': 'Zara', 'dept': 'IT'},
  'E003': {'name': 'Usman', 'dept': 'Finance'},
  'E004': {'name': 'Noor', 'dept': 'IT'}
}

emp_dir.update({'E005':{'name':'Ans','dept':'IT'}})
# print(emp_dir)
print('These are the employees in IT department')
for emp_id,obj in emp_dir.items():
    if obj['dept']== 'IT':
        print(obj['name'])