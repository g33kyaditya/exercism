import math

class Allergies:
    dic = {}
    dic['eggs'] = 1
    dic['peanuts'] = 2
    dic['shellfish'] = 4
    dic['strawberries'] = 8
    dic['tomatoes'] = 16
    dic['chocolate'] = 32
    dic['pollen'] = 64
    dic['cats'] = 128

    def __init__(self, val):
        self.val = val
        self.lst = []
        while val != 0:
            closestRoot = math.floor(math.log(val, 2))
            for k in Allergies.dic:
                if Allergies.dic[k] == 2**closestRoot:
                    self.lst.append(k)
            val = val - 2**closestRoot


    def is_allergic_to(self, allergy):
        if Allergies.dic[allergy] <= self.val:
            return True
        return False

print Allergies(257).lst
