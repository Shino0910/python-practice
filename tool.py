# function of for 
"""""
def power(x,y):
    result = x
    for index in range(y-1):
        result= result * x
    return result


print(power(2,5))

"""

#class
"""""
class phone:
    def __init__(self, os, number, is_waterproof):
        self.os= os
        self.number=number
        self.is_waterproof=is_waterproof


phone1= phone("ios","123","True")

"""""


class question:
    def __init__(self,description, anwer):
        self.description = description
        self.answer = anwer



