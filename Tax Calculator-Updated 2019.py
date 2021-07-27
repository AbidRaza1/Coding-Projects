
## SALES TAX CALCUALTOR FOR CANADIAN PROVINCES

print('In order to calculate total cost of your order including taxes, please enter the acroynm of the state you live \n ')
print(' Alberta-AB \n British Columbia-BC \n Manitoba-MB \n NorthWestTerritories-NWT \n Nunavut-NU \n NewFoundLand and Labradour-NL \n NewBrunswick-NB \n NovaScotia-NS \n Ontario-ON \n Prince Edwards Island- PEI \n')

province = input('Please enter your province: ').upper()
Orderamount = float(input('Please enter your order amount $'))
TA =  Orderamount + (Orderamount * (0.05))
TB =  Orderamount + (Orderamount * (0.15))
TC =  Orderamount + (Orderamount * (0.13))
TD =  Orderamount + (Orderamount * (0.12))
TE =  Orderamount + (Orderamount * (0.14975))

if province == 'AB' or 'NWT' or 'YT' or 'NU':
    print('Your total amount is $' + str(TA))
elif province == 'NL' or 'NB' or 'NS' or 'PEI':
    print('Your total amount is $' + str(TB))
elif province == 'MB' or 'ON':
    print('Your total amount is $' + str(TC))
elif province == 'BC':
    print('Your total amount is $' + str(TD))
elif province == 'QC':
    print('Your total amount is $' + str(TE))
else:
    ('The province you entered does not belong to Canada, Please try again')

