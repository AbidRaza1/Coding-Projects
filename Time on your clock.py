
#Time on your clock after wait a particular wait time

c = int(input('Please enter the time on your 24HR clock: '))

w = int(input('Please enter the wait time to ring the alarm: '))

t = (c + w) % 24

print('Time on your clock after wait time of:', w, 'would be: ','' ,t)

