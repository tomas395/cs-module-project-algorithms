'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    left = 0
    r = len(arr) - 1

    while left <= r:  # if theres a zero in the left, swap by reassigning the placement of the index by +1 or -1
        if arr[left] == 0 and arr[r] != 0:
            arr[left], arr[r] = arr[r], arr[left]
            left += 1
            r -= 1
        else:
            if arr[left] != 0:  # don't do anything and continue evaluating
                left += 1  # move left one spot
            if arr[r] == 0:
                r -= 1  # pull right back one spot
    return arr

# i know im going to want to iterate over every index in the list and find the ones with the value of 0
# if i delete them, i can push them and it will apply them to the last index when appeneded, so do that like you would in js
    # for el in arr:
    #     if el == 0:
    #         arr.remove(0)
    #         arr.append(0)
    # return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
