import datetime
now = datetime.datetime.now()
if now.hour < 12:    
    print(' Please Read from our Breakfast menu: \n ')
    print(' PanCakes \n')
    print(' Side Dish Today: \n')
    print(' Yougurt \n')

    print('Please type your order please \n')
    Main = input('Enter the main dish or enter None: \n').upper()
    Side = input('Enter the side dish: \n').upper() 
    pc = 5
    s = 2
    if Main == 'None' and Side == 'None':
        print('Your order has not been placed please try again \n')
    elif Main == 'PANCAKES' and Side == 'YOUGURT':   
        print('Your order cost is $' + str(pc + s) +'\n')
    elif Main == 'NONE' and Side == 'YOUGURT':
        print('Your order cost is $' + str(s) + '\n')
    elif Main == 'PANCAKES' and Side == 'NONE':
        print('Your order cost is $' + str(pc) + '\n')
    else:
        print('Have a  wonderful day' + '\n')
else:
    print('thanks')

