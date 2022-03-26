from math import *

## Returns the mean for values of a dictionary
class Mean():
    def __init__(self) -> None:
        pass
    def get(self, a: dict) -> int:
        mean = 0
        eff = 0
        for i in a:
            mean += i * a[i]
            eff += a[i]
        mean /= eff
        return mean 
## Returns the variance equation and typicalGap for a dictionary

class Variance():
    def __init__(self) -> None:
        pass 
    def get(self, a: dict) -> int:
        mean = Mean()

        var = 0
        total = 0
        aMean = mean.get(a)

        for i in a: 
            v = a[i]
            var += (v*((i-aMean)**2))
            total += v

        var /= total
        return var

    def typicalGap(self, a: int) -> int:
        return sqrt(a);
      
## Returns a medianne of a dictionary values
class Medianne():
    def __init__(self) -> None:
        pass
    def get(self, a: dict) -> int:
        total = 0
        med = 0
        b = []

        for i in a:
            for c in range(int(a[i])):
                b.append(i)

        b = sorted(b)
        total = len(b)

        if total % 2 != 0: 
            med = b[round(total/2)]
        else:
            med = (b[(round(total/2))] + b[round((total/2)+1)]) / 2

        return med

## Checks if a value of a list is inside an intervall defined respectively by x(+-)2o
def CheckListOnI(x, o, l: list) -> int:
    start = x - (2*o)
    end = x + (2*o)

    inList = []
    total = 0

    for i in l: 
        if (l[i] >= start and l[i] <= end): 
            inList.append(l[i])
            total += 1

    return round(total/len(l) * 100, 3)
