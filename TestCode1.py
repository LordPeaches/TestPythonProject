print('Hello World')

x = 5
y = 42
z = x + y

print('z is:', z)

print('Hey bub screw u buddy')
print('Whats 9 + 10?')
print('Fuck you reply to me')

# Takes a start and end values, and computes the sum off all multiples of m
def sum_mult_in_range(start, end, m):
    list_range = range(start, end + 1)
    sum_list = 0
    for x in list_range:
        if x % m == 0:
            sum_list +=  x
    return sum_list

start = 5
end = 25
m = 5
print(sum_mult_in_range(start, end, m))