def _input(number, input_type):
    while True:
        try:
            return input_type(input(number))
        except:
            pass

def output_statement(savings, year, starting_amount, interest_earned):
    print(f'Year {year + 1}')
    print('-----------------')
    print(f'Starting amount: {starting_amount}')
    print(f'Interest earned: {interest_earned}')
    print(f'Total savings: {savings}')
    print()

savings = _input('Please enter your starting savings: ', int)
nr_years = _input('How many years will you be saving? ', int)
interest_rate = _input('What is your interest rate? ', float)
interest_rate = round(interest_rate / 100, 3)
print()

for year in range(nr_years):
    starting_amount = savings
    interest_earned = round(savings * interest_rate, 2)
    savings = round(savings + interest_earned, 2)
    output_statement(savings, year, starting_amount, interest_earned)
