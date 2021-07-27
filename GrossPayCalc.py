
import sys as s

hrs = input("Enter Hours:")

hourlyrate = input("Enter rate per hour:")

try: 
    
    hrs = float(hrs)
    
    hourlyrate = float(hourlyrate)

except:
    
    print('Please type numbers')
    
    s.exit()    

if hrs > 40:
            
        Ot = hrs - 40
            
        GrossPay = (40 * hourlyrate ) + (Ot *hourlyrate* 1.5)

else:
        
        GrossPay = hourlyrate * hrs

print(GrossPay)






