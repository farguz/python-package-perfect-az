from more_itertools import sliced, substrings

def half(num):
    return num / 2

subs = [''.join(s) for s in substrings('more')]
print(subs)

slices = list(sliced((1, 2, 3, 4, 5, 6, 7, 8), 3))
print(slices)
