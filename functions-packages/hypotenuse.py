import math   
def get_hypotenuse(catet1, catet2):  
    # calculate hypotenuse of right triangle based on 2 catets and return it
    sqrthypotenuse = catet1 * catet1 + catet2 * catet2
    hypotenuse = math.sqrt(sqrthypotenuse)
    return hypotenuse

