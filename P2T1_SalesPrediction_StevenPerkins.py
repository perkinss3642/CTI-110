# This program calculates projected annual profit
# April 1, 2019
# CTI-110 P2T1 - Sales Prediction
# Steven Perkins

# User enters projected total sales.
projected_total_sales = float(input("projected total sales"))

# Calculate the projected annual profit.
projected_annual_profit = .23 * projected_total_sales

# Display projected annual profit.
print ("The projected annual profit is", \
       format(projected_annual_profit, ".2f"))


