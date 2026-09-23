#Using the range() Function
for value in range(1, 6):
    print(value)

 #Using range() to Make a List of Numbers
number = list(range(6))
print(number)

#######
number = list(range(2,17, 3))
print(number)


#using range() to add in a list
squares = []
for value in range(1, 12):
    square = value **2
    squares.append(square)
print(squares)


#Simple Statistics with a List of Numbers.
digit = [1,2,3,4,5]
min(digit)
sum(digit)
max(digit)

