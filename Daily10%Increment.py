capital = int(input("What is your capital: "))
Targeted_Attempts = int(input("How many attempts: "))
Total_Payout = 0
x = 1
while x <= Targeted_Attempts:
    # if x%7 != 0:
        capital *= 1.10
        print("Day",x,"Capital is:",capital)
    # else:
    #     payout = capital * 0.5
    #     print("Day",x,"Weekly Payout: ",payout)
    #     capital = capital - payout
    #     Total_Payout += payout
    #     print("------------------------")
    #     print("Now, Capital is",capital)
        x += 1
# print("Total Weekly Payout is:",Total_Payout)