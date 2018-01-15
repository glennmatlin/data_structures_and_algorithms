# URL: https://www.hackerrank.com/challenges/ctci-ransom-note/problem

from collections import Counter

input_zero = """
6 4
give me one grand today night
give one grand today
"""

input_one = """
6 5
two times three is not four
two times two is four
"""

def ransom_note(magazine, ransom):
    magazine_counter = Counter(magazine)
    ransom_counter = Counter(ransom)
    # print(magazine_counter)
    # print(ransom_counter)
    counter_difference = ransom_counter - magazine_counter
    if any(counter_difference) > 0:
        return False
    else:
        return True


m, n = map(int, raw_input().strip().split(' '))
magazine_input = raw_input().strip().split(' ')
ransom_input = raw_input().strip().split(' ')
answer = ransom_note(magazine_input, ransom_input)

if answer:
    print("Yes")
else:
    print("No")

