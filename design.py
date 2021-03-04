from math import pi, log10, sqrt
import numpy as np
import matplotlib.pyplot as plt


# Setting constants
c = 3.0e8
eps_ap = 0.51


class Horn() :
    def __init__(self, A,a,b) :
        self.A = A
        self.a = a
        self.b = b
        self.compute_carac()

    def __str__(self) :
        return self.affiche()
    
    def compute_carac(self) :
        self.B = 0.5*(self.b + sqrt(self.b**2 + 8/3*self.A*(self.A-self.a)))
        self.R_H = self.A*(self.A-self.a)/(3*wavelength)
        self.L_A = sqrt(self.R_H**2 + (self.B-self.b)**2)
        self.L_B = sqrt(self.R_H**2 + (self.A-self.a)**2)

        self.Gain = 10*log10(4*pi*eps_ap*self.A*self.B/pow(wavelength,2))

    def test_frequency(self) :
        lambda_c = 2*self.a 
        nu_c = c/lambda_c
        nu_min = 1.25*nu_c
        nu_max = 1.9*nu_c
        print("The horn frequency limits are : ", round(nu_min*1.e-6,2), 'Mhz < nu < ',  round(nu_max*1.e-6,2), 'Mhz')
        if nu_min<freq_wave<nu_max :
            print('Your frequency nu =', round(freq_wave*1.e-6,2), 'Mhz is OK with those a and b\n')
        else :
            print('Your frequency nu =', round(freq_wave*1.e-6,2), "Mhz doesn't belongs to this interval\n")

    def affiche(self) :
        attr = ['A', 'B', 'a', 'b', 'L_A', 'L_B', 'R_H', 'Gain']
        form = "{0:12}{1:12}{2:12}{3:12}{4:12}{5:12}{6:12}{7:12}"
        carac = [str(round(100*self.A,2)), str(round(100*self.B,2)), str(round(100*self.a,2)), str(round(100*self.b,2)), str(round(100*self.L_A,2)), str(round(100*self.L_B,2)), str(round(100*self.R_H,2)), str(round(self.Gain,2))]
        
        return('Characteristics of the GalaxyClock : \n' + form.format(*attr)+'\n'+ form.format(*carac))


#Wave caracteristics
freq_wave = 1.4204e9
wavelength = c/freq_wave

#Parameters of the horn (in m)
a = 16.3e-2
b = 10.5e-2
A = 49e-2

Galacticlock = Horn(A,a,b)
Galacticlock.test_frequency()
print(Galacticlock)