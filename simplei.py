def calculate_simple_interest(principal, time, gender, senior_citizen):
    if gender == 'female' and senior_citizen:
        rate = 8
    elif gender == 'female' and not senior_citizen:
        rate = 6
    elif gender == 'male' and senior_citizen:
        rate = 7
    else:
        rate = 5
    
    interest = (principal * rate * time) / 100
    return interest


# Example usage
principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time period (in years): "))
gender = input("Enter the gender (male/female): ")
senior_citizen = input("Are you a senior citizen? (yes/no): ")

if senior_citizen.lower() == "yes":
    senior_citizen = True
else:
    senior_citizen = False

interest = calculate_simple_interest(principal, time, gender.lower(), senior_citizen)
total_amount = principal + interest

print("Interest:", interest)
print("Total amount:", total_amount)
