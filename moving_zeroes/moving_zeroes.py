'''
Input: a List of integers
Returns: a List of integers
'''

# i know im going to want to iterate over every index in the list and find the ones with the value of 0
# if i delete them, i can push them and it will apply them to the last index when appeneded, so do that like you would in js


def moving_zeroes(arr):
    for el in arr:
        if el == 0:
            arr.remove(0)
            arr.append(0)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
