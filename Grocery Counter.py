

# GROCERY COUNTER


# Initializing loop

nitems = 0
ncount =0
more = True

# Checking for more items

while more:
            x = float(input('Enter item price or zero if no item is left: '))
            if x > 0 and x != 0:
                    nitems =  x + nitems
                    ncount =  1 + ncount
            else:
                 break
# Printing price and items

print('Total Price',nitems)
print('Total Items',ncount)



