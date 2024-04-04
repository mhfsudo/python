from fractions import Fraction

class FolgenUndGrenzwerte:

    def _harmonic(self):
        n=1
        while True:
            yield Fraction(1,n)
            n+=1
    
    def RunHarmonic(self,count):
        runCount = 0
        for value in self._harmonic():  
            print(value)
            runCount+=1
            if runCount == count:
                break


    def SomeValues(self,seq, L =[10 ** k for k in range(10)]):
        for n in L:
            print("{:>15}: {}".format(n,seq(n)))



# Driver code to check above generator function
# 
folgen = FolgenUndGrenzwerte()
folgen.RunHarmonic(20)

folgen.SomeValues()

