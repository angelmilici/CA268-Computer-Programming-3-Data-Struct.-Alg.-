import sys

int_num = []
num = []

def main():
    for i in range(0, 101):
        int_num.append(i)

    num.append('zero')
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    for word in digits + teens:
        num.append(word)

    for tens_word in tens:
        num.append(tens_word)

        for digits_word in digits:
            num.append(tens_word + '-' + digits_word)

    num.append('one hundred')

    dictionary = dict(zip(int_num, num))

    for line in sys.stdin:
        b = []
        for i in line.strip().split():
            b.append(dictionary[int(i)])
        print(' '.join(b))

if __name__ == '__main__':
    main()
