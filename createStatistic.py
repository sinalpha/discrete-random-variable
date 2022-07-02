import matplotlib.pyplot as plt
import numpy as np

def createStatic(RV, pro, colLen):
    fileName_ = "src/output.jpg"
    x = np.arange(colLen) 
    plt.bar(x, pro)
    plt.xticks(x, RV)
    plt.savefig(fileName_)