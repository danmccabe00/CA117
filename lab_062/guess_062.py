from random import randint

top = 1000000
bottom = 0
z = randint(bottom, top)

def guess(g):
    if g == z:
        return 0
    elif g < z:
        return -1
    else:
        return 1

# Find z *efficiently* by calling guess() (and without peeking at z!)
def find():
    t = top
    b = bottom
    while b < t:
        mid = (b + t) // 2
        g = guess(mid)
        if g == 0:
            return mid
        elif g == -1:
            b = mid + 1
        elif g == 1:
            t = mid
    return b

def main():
    a = find()
    if a == z:
       print('Correct!')
    else:
       print('Incorrect!')
    print('You said {:d} and answer is {:d}'.format(a, z))
if __name__ == '__main__':
    main()
