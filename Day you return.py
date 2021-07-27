
# Calculating the return date.

calender = print('Calendar days:','Sudnay-Saturday:', '0-6')

# Asking user to enter the day he wants to leave

day = int(input('Please enter number of day you are planning to leave from calender '))

# Asking user to enter the number of days for leave

length = int(input('How long would you like to stay(No.of days) '))

# Calculating return day 

t = (day + length) % 7

# Printing results

print('You will return on ', t, "calenday day of the week")
