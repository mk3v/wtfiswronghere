"""
We will use this script to teach Python to absolute beginners
The script is an example of Fizz-Buzz implemented in Python

The FizzBuzz problem: 
For all integers between 1 and 99 (include both):
    # print fizz for multiples of 3
    # print buzz for multiples of 5 
    # print fizzbuzz for multiples of 3 and 5"
"""
import fizzbuzz

def fixbuzz(maxNum):

    for i in range(1, maxNum):
        if i % 3 == 0 and i %5 == 0:
            print(i, 'fizzbuzz')
        elif i % 3 == 0:
            print(i, 'fizz')
        elif i % 5 == 0:
            print(i, 'buzz')


#----START OF SCRIPT
if __name__=='__main__':
    fizzbuzz(100)