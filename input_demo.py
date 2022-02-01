'''
In a team of 20 members, some members are taken
and want to display the numbers that are not taken
so that others don`t pick the picked numbers
'''

#Taken numbers
numTaken = [3, 5, 7, 11, 13]

print("Available numbers :")

#Loop
for i in range(1, 25):
    if i in numTaken:
        continue
    print(i)