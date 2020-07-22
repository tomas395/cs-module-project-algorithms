'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

# we're going to need a way to iterate through the list
# we're going to need to a find a way to return the single instance of the element through a conditional


def single_number(arr):
    for el in arr:
        if arr.count(el) == 1:
            return el


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
