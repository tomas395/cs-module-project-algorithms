# Product of All Other Numbers

'''
Input: a List of integers
Returns: a List of integers
'''
# Write a function that receives an array of integers and returns an array consisting of the product of
# all numbers in the array _except_ the number at that index.

# For example, given
# ```
# [1, 7, 3, 4]
# ```
# your function should return
# ```
# [84, 12, 28, 21]
# ```
# by calculating
# ```
# [7*3*4, 1*3*4, 1*7*4, 1*7*3]
# ```
# In the above example, the final value at index 0 is the product of every number in the input array _except_ the number at index 0.
# Can you do this in `O(n)` time with `O(1)` space _without_ using division?


# we're going to need an additional array to hold our final value
# we'll want to iterate over the entire length of the array
# we'll need a counter
# we're going to need to multiply and append that pointer at some point
# loop through it again and compare to the first
# append the multplied value and append it to the array

def product_of_all_other_numbers(arr):
    total_arr = []  # this will hold the values of each item
    for i in range(len(arr)):  # iterate over the length of the array
        counter = 1  # this variable to hold the value of the number
        for n in range(len(arr)):
            # nesting a for loop and if n is different from the current number THEN you
            if (n != i):
                # if the counter is not equal to the array, multiply it by the counter or otherwise ignore it
                counter = counter * arr[n]
        total_arr.append(counter)
    return total_arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
