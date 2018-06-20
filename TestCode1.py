print('Hello World')

x = 5
y = 42
z = x + y

print('z is:', z)

print('Hey bub screw u buddy')
print('Whats 9 + 10?')
print('REPLY TO MEEEEEEEEEEEEEEEEEEE')

# Takes a start and end values, and computes the sum off all multiples of m
def sum_mult_in_range(start, end, m): #This is the method declaration

    list_range = range(start, end + 1) #This creates a list from Start to (end + 1), called 'list_range'
    sum_list = 0
    
    for x in list_range: #Starts iterating through our list, storing each value as 'x'
        if x % m == 0: #If statement using Modulo
            sum_list +=  x #Notice how sum_list must be declared outside the loop? Important concept
    
    return sum_list #Returns our list

start = 5
end = 25
m = 5
print(sum_mult_in_range(start, end, m)) #Call the method by its name, imports some variables, and prints out the return value