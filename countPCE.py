import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as cnst

def notBadFunction(FF, Voc, Jsc, Proc):
    """
        :FF = [%]:
        :Voc = [V]:
        :Jsc = [mA/cm2]:
        :Proc - часть от излучения [0..1]:
    """

    if Proc < 0 or Proc > 1:
        return 'От 0 до 1. Вводите часть от излучения.'
    Pin = 100 * Proc # Pin = [mW/cm2]
    return (FF * Voc * Jsc) / Pin

print(notBadFunction(60.812, 0.968, 11.194, 1)) # данные взяты из файла на google disk
