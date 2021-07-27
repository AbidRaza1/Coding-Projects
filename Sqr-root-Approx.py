# Defining Square root function

def mySqrt(n):
        
        fG = n/2
       
        for i in range(5):
                   
                    g = (0.5) * (fG + (n/fG))
                    
                    fG = g
        return g

# Asking user input

n = int(input("Enter the Number(Except 0): "))

# Printing squareroot 

print(mySqrt(n))   
