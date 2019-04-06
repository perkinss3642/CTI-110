#Tip calculator
#April 6, 2019
#CTI-110 P2HW2 - Meal Tip Calculator
#Steven Perkins

#Enter the meal cost
meal_cost = float(input("Enter cost:"))

#Calculate tip amounts
fifteen_tip = meal_cost*.15
total_cost_one = meal_cost+fifteen_tip
eighteen_tip = meal_cost*.18
total_cost_two = meal_cost+eighteen_tip
twenty_tip = meal_cost*.20
total_cost_three = meal_cost+twenty_tip

#Display tip amounts
print("15% Tip is", \
      format(fifteen_tip, ".2f"))
print("Total cost with 15% tip is", \
      format(total_cost_one, ".2f"))
print("18% Tip is", \
      format(eighteen_tip, ".2f"))
print("Total cost with 18% tip is", \
      format(total_cost_two, ".2f"))
print("20% Tip is", \
      format(twenty_tip, ".2f"))
print("Total cost with 20% tip is", \
      format(total_cost_three, ".2f"))

