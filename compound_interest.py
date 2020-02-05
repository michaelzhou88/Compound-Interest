# Estimated yearly interest 

# Function that calculates the compound interest based on the user's inputs
def compound_interest(principal_amount, interest_rate, years):
    result = (principal_amount * pow((1 + interest_rate),years))
    return result


# Prompting user to enter the principal amount to start off with 
print('How much money is currently in your account')
principal_amount = float(input('Enter amount in pounds and pence: '))

# Prompts user to the enter their annual interest rate
print("What do you estimate will be the yearly interest of this investment? ")
interest_rate = float(input('Enter interest in decimal numbers : (e.g. 10% = 0.1) '))

# Prompts user to enter the number of years they intend to the save for
print('How many years will you be save?')
years = float(input('Enter years: '))

print('')

# Invokes the compound_interest function to perform the calculation
final_amount = round((compound_interest(principal_amount, interest_rate, years)),2)

# Outputs result
print("In " + str(int(years)) + " years, your balance would be: £" + str(final_amount))



