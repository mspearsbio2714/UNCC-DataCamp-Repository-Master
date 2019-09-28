# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    #gives the total count of numbers
    length = len(numbers)

    #Initialize my total variable
    total = 0.0

    #for sums all the numbers within the list
    for number in numbers:
        total += number

     # Returns the sum divided by the length   
    return total / length


# Test your function with the following:
print(average([1, 5, 9]))

