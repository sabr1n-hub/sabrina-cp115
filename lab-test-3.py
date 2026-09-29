# Programmer's name= Sabrina Sofea
# Problem Description:
# Usage < RM 50 per month, No discount will be given
# Usage < = RM100 per month, Get a 5% discount
# Usage > RM 100 per month, Get a 20% discount
monthly_usage =float(input("Enter monthly usage:"))
if monthly_usage < 50.0:
    discount = 0.0
elif monthly_usage <= 100.0:
    discount=0.05
else:
    discount=0.20
total_discount= monthly_usage*discount
bill_amount= monthly_usage - total_discount
print(bill_amount)
