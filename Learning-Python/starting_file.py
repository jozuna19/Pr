# if the bill was $150.0 split between 5 people, with 12% tip
#Each person should pay (150.00 / 5) *1.12

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? "))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15 ?"))
people = int(input("How many people to split the bill? "))

bill_w_tip = ((bill * (percent/100)) + bill)

bill_pp = (bill_w_tip / people)
final_amt = "{:.2f}".format(bill_pp)

print(f"Each personal should pay ${final_amt}.")
