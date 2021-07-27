


postalcode = ''
postalcode = input('Enter your postal code:').upper()
print(postalcode)
import datetime
userinput1 = input('Please enter the date you are available to volunteer(dd/mm/yyyy)')
userinput2 = input('Please enter the last date you will be availble to volunteer(dd/mm/yyyy)')
VolunteerDate1 = datetime.datetime.strptime(userinput1,'%d/%m/%Y')
VolunteerDate2 = datetime.datetime.strptime(userinput2,'%d/%m/%Y')
days = VolunteerDate2 - VolunteerDate1
print('Start Date to Volunteer : ' + str(userinput1))
print('End Date to Volunteer : ' + str(userinput2))
print('Number of days avaiblale to volunteer are : ' + str(days.days))
print('The volunteer opportunities available in the following counties nearby' + ' ' + str(postalcode) + ' ' + 'in the period you mentioned are: \n')
print(' 1-Strathcona County \n 2-Sherwood County \n 3-Stettler County \n 4-Drumheller County') 
print('Please check their websites for more details')




