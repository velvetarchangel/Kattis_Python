a, b = [int(x) for x in input().split()]

even_array = [] # array of integers that are produced as a result of rec_even
odd_array = [] # array of integers that are produced as a result of rec_odd
count_even = 0
count_odd = 0


def rec_even(even_int):
    step = even_int/2 # the result of the recursive step
    if step == 1:
        return 1
    else:
        even_array.append(step)
        return(rec_even(step))

def rec_odd(odd_int, even_array):
    step = 3* odd_int + 1
    for i in range(even_array):
        if step == even_array[i]:
            return step
        else:
            odd_array.append(step)
            return(rec_odd(step,even_array))
