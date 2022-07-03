import math 

def variance1(RV, pro):
    sum, excepted_ = 0,  excepted(RV, pro)
    for RV_, pro_ in zip(RV, pro):
        sum += ((RV_ - excepted_) ** 2) * pro_
    return sum

def variance2(RV, pro):
    RVSquare = [ i**2 for i in RV]
    return excepted(RVSquare, pro) - excepted(RV, pro) **2
    

def excepted(RV, pro):
    sum = 0
    for RV_, pro_ in zip(RV, pro):
        sum += RV_ * pro_
    return sum

def SD(RV, pro):
    return math.sqrt(variance1(RV, pro))
