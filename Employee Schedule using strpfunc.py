#Importing datetime library

import datetime 

# Asking user to input employees name and their scheduling dates

Emp1 = input('Please enter name of employees to work in Bakery').upper()
Emp2 = input('Please enter name of employees to work at FrontEnd').upper()
Emp3 = input('Please enter name of employees to work as Runner').upper()
Emp4 = input('Please enter name of employees to work in DriveThru').upper()
Emp5 = input('Please enter name of employees to work on FryerStation').upper()
Emp6 = input('Please enter name of employees to work in CashHandling').upper()
todaydate = input('Please enter the schedule start date(mm/dd/yyyy)')
enddate =   input('Please enter the schedule end date(mm/dd/yyyy)')

# Formatting date time object using strptime() function

current  = datetime.datetime.strptime(todaydate, '%m/%d/%Y')
end = datetime.datetime.strptime(enddate, '%m/%d/%Y')

# Calculating schedule days

scheduledays = end  -  current

# Printing Schedule and Depatrment and in which each employee will be deployed

print('Following is the schedule for next' + ' ' + str(scheduledays.days)+ 'days \n')
print(str(Emp1) + ' ' + 'is going to work in Bakery \n')
print(str(Emp2) + ' ' + 'is going to work in FrontEnd \n')
print(str(Emp3) + ' '+ 'is going to work in Runner \n')
print(str(Emp4) +' ' + 'is going to work in DriveThru \n')
print(str(Emp5) +' ' + 'is going to work in FryerStation \n')
print(str(Emp6) +' ' +'is going to work in CashHandling')














