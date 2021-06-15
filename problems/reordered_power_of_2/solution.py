from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = len(str(n))
        print(digits)
        #powers = set()
        c = Counter(str(n))
        power = 1
       # powers.add(1)
        while True:
            
            if len(str(power)) == digits:
                #powers.append(power)
                if c == Counter(str(power)):
                    return True
                power = power << 1
            elif len(str(power)) < digits:
                power = power << 1
                continue
            else:
                break
            
        #print(powers)
        return False
        #for power 