annual_salary= float(input("Enter your annual salary: "))
portion_saved= float(input("Enter the percent of your salary to save in (decimal): "))
total_cost= float(input("Enter the cost of your dream house: "))
semi_raise= float(input("Enter the semi annual raise in (decimal): "))

annual_return= 0.04
down_payment= 0.25 * total_cost
savings= 0
months= 0

monthly_salary= annual_salary/12
monthly_rate= annual_return/12
#we are taking the annual return as the interest rate from the bank after putting monthly salary to save .

while savings< down_payment:
    #inside the while loop as the monthly savinging changes after every 6 months
    monthly_saving= monthly_salary * portion_saved
    
    savings+= savings*monthly_rate+monthly_saving
    months+= 1
    #increase in salary after every 6 months
    if months%6==0:
        monthly_salary+= monthly_salary*semi_raise

print("Number of months: ", months)