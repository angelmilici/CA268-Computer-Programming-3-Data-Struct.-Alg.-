from random import randint

# Find z *efficiently* by calling guess() (and without peeking at z!)
def find():
    top = 1000000
    bottom = 0
    while top > bottom:
        mid = int((top + bottom) / 2)
        guessed = guess(mid)

        if guessed == 1:
            top = mid

        elif guessed == -1:
            bottom = mid

        else:
            return mid

def main():
    a = find()
    if a == z:
        print('Correct!')
    else:
        print('Incorrect!')
    print('You said {:d} and answer is {:d}'.format(a, z))

if __name__ == '__main__':
    main()
