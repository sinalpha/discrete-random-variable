import math 

def variance1(RV, pro):
    sum, mean_ = 0,  mean(RV, pro)
    for RV_, pro_ in zip(RV, pro):
        sum += ((RV_ - mean_) ** 2) * pro_
    return sum

def variance2(RV, pro):
    RVSquare = [ i**2 for i in RV]
    return mean(RVSquare, pro) - mean(RV, pro) **2
    

def mean(RV, pro):
    sum = 0
    for RV_, pro_ in zip(RV, pro):
        sum += RV_ * pro_
    return sum

def SD(RV, pro):
    return math.sqrt(variance1(RV, pro))
