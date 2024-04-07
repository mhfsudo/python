#import fast timer
from timeit import default_timer as timer
#import sys
#sys.setrecursionlimit(10000)

# 1. Implementation of two functions which calculate the n-the Fibonacci number. One iterative the other recursive.
# class to calculate the fibonacci numbers
class Fibonacci:

    _fibArray = [0, 1]
    _usedTime = 0

    def getNTheFibonacciNumberRecursive(self, n):
        start = timer()
        result = self._fibonacciRecursive(n)
        stop = timer()
        fib.calcTime(start,stop)
        return result

    # Get the n-the fibonaccinumber iterativ
    def getNTheFibonacciNumberIterative(self, n):
        start = timer()
        
        nextterm = 0
        present = 1
        previous = 0

        # Get only values greater than 0
        if n < 0:
            print("Incorrect input")

        i = 0
        while i < n:
            nextterm = present + previous
            present = previous
            previous = nextterm
            i += 1 

        stop = timer()
        self.calcTime(start,stop)
        return nextterm

    def calcTime(self, startTime, stopTime):
        self._usedTime = (stopTime-startTime)

    def getUsedTimeToCalculateNtheNumber(self):
        return self._usedTime

    # private get the n-the fibonaccinumber recursive
    def _fibonacciRecursive(self, n):
        retVal = 0
        # Get only values greater than 0
        if n < 0:
            print("Incorrect input, n has to be greater than 0")           
        # First Fibonacci number is 0
        elif n == 0:
            retVal = 0
        # Second Fibonacci number is 1
        elif n == 1:
            retVal = 1
        else:
            retVal = self._fibonacciRecursive(n - 1) + self._fibonacciRecursive(n - 2)
        return retVal


# create instance of class
fib = Fibonacci()

#Get Input from user
#set the n-the fibonaccinumber you would like to get.

number = 1

#At position 10 is Fibonacci number 100
print("\n")
print("Recursive calculation of the Fibonacci Number")
#print(f"At position {number} is Fibonacci number: {fib.getNTheFibonacciNumberRecursive(number)} \nProcess time: {fib.getUsedTimeToCalculateNtheNumber()*1000}ms")

print("\n")
print("Iterative calculation of the Fibonacci Number:")
print(f"At position {number} is Fibonacci number: {fib.getNTheFibonacciNumberIterative(number)}")
print(f"Process time: {fib.getUsedTimeToCalculateNtheNumber()*1000}ms")

print("\n")
print("end")
print("\n")


# see how to use time
# https://stackoverflow.com/questions/7370801/measure-time-elapsed-in-python


# https://www.geeksforgeeks.org/private-methods-in-python/

# https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series
