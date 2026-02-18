'''Collaboration:
1. Suneethra
2.Vaibhav 
3.Rathin
4.Sadhana'''


annual_salary= float(input("Enter the starting salary: "))
#given constants
total_cost= 1000000
annual_return= 0.04
semi_raise= 0.07
months= 36
down_payment= 0.25 * total_cost
low= 0.0 #no savings
high= 1.0 #full savings
step= 0

# Function to calculate savings 
def calculate_savings(rate):
    savings= 0
    monthly_salary= annual_salary/12
    monthly_rate = annual_return/12
    month= 1

    while month<=months:
        #compund interest and monthly saving
        savings+= savings*monthly_rate
        savings+=monthly_salary*rate
        #increase in salary after every 6 months
        if month%6==0:
            monthly_salary+= monthly_salary* semi_raise

        month+= 1
    return savings

#to check if it is possible to pay the down payment in three years with 100% savings
max_savings= calculate_savings(1.0)
#100% of the savings 

if max_savings<down_payment:
    print("It is not possible to pay the down payment in three years.")
else:
    # Bisection search starts here
    while True:
        step+= 1 #counting the number of guesses
        mid= (low+high)/2
        savings= calculate_savings(mid)
        if abs(savings-down_payment)<= 100:
            #we found the correct rate within $100
            #stop searching
            break
        elif savings<down_payment:
            #new mid, we need to save more
            low=mid
        else:
            #new mid, we need to save less
            high=mid

    print("The best savings rate: ", round(mid, 2)) #rounding off to 2 decimals
    print("Steps of bisection search: ", step)