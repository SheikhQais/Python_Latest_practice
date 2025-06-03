try:
    numerator = int(input("Enter numerator: "))
    deno = int(input("Enter Denomenator: "))
    number = numerator/deno
except ValueError:
        print("You can enter anyting other than Number")
except ZeroDivisionError:
        print("You cannot divide numerator by 0")
else:
    print("Here is the result:",int(number))
finally:
    print("Operation complete")