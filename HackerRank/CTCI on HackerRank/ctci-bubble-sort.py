# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

def bubble_sort(array_n, array):
    num_swaps = 0

    for x in range(array_n):
        for y in range(0, n-x-1):
            if array[y] > array[y + 1]:
                array[y], array[y+1] = array[y+1], array[y]
                num_swaps += 1

    first_element = array[0]
    last_element = array[-1]

    print 'Array is sorted in {} swaps.'.format(num_swaps)
    print 'First Element: {}'.format(first_element)
    print 'Last Element: {}'.format(last_element)


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

bubble_sort(n, a)
