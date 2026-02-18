annual_salary= float(input("Enter your annual salary: "))
portion_saved= float(input("Enter the percent of your salary to save in (decimal): "))
total_cost= float(input("Enter the cost of your dream house: "))


down_payment= 0.25*total_cost #the installment of the house we have to pay in the start
savings= 0
months= 0

monthly_salary= annual_salary/12
monthly_rate= 0.04/12 #the rate of return (interest given) from the bank after saving the money
monthly_saving= monthly_salary*portion_saved #amount of money saved from monthly salary

while savings< down_payment: #whle the savings is less than the down payment we have to pay

    savings+=(savings*monthly_rate)+monthly_saving
    months+= 1

print("Number of months:", months)