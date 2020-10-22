import numpy as np
import matplotlib.pyplot as plt

#Modelo de perda de carha definido por Bellos, Nalbantis, Tsakiris
'''
Bellos, Vasilis; Nalbantis, Ioannis; Tsakiris, George (December 2018). "Friction Modeling of Flood Flow Simulations". Journal of Hydraulic Engineering. 144 (12): 04018073. doi:10.1061/(asce)hy.1943-7900.0001540. ISSN 0733-9429.
Bellos, Vasilis; Nalbantis, Ioannis; Tsakiris, George (2020-10-01). "Erratum for "Friction Modeling of Flood Flow Simulations" by Vasilis Bellos, Ioannis Nalbantis, and George Tsakiris". Journal of Hydraulic Engineering. 146 (10): 08220005. doi:10.1061/(ASCE)HY.1943-7900.0001802. ISSN 1943-7900.
'''
def f(Re, e_r):
    '''
    :param Re: Número de Reynolds []
    :param e_r: Rugosidade relativa e/D []
    :return: Fator de fricção []
    '''
    #Cálculo do coeficiente a:
    a = 1 / (1 + ((Re / 2712)**8.4))
    #Cálculo do coeficiente b:
    b = 1 / (1 + ((Re / (150 * e_r))**1.8))
    #Cálculo do fator de fricção:
    return ((64 / Re)**a) * ((0.75 * np.log(Re / 5.37))**(2 * (a - 1) * b)) * ((0.88 * np.log(3.41 * e_r))**(2 * (a - 1) * (1 - b)))

