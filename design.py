from math import pi, log10, sqrt

c = 3.0e8

#Caracteristics of the wave
freq_wave = 1.4204e9
wavelength = c/freq_wave

#Definition of the parameters of the horn (in m)
a = 16.3e-2
b = 10.5e-2
A = 60.e-2

def frequency_limits(a, b, nu) :
    lambda_c = 2*a 
    nu_c = c/lambda_c
    nu_min = 1.25*nu_c
    nu_max = 1.9*nu_c
    return [nu_min,nu_max]

def test_frequency(nu, f_lim) :
    nu_min,nu_max = f_lim
    print("The horn frequency limits are : ", round(nu_min*1.e-6,2), 'Mhz < nu < ',  round(nu_max*1.e-6,2), 'Mhz')
    if nu_min<nu<nu_max :
        print('Your frequency nu =', round(nu*1.e-6,2), 'Mhz is OK with those a and b\n')
    else :
        print('Your frequency nu =', round(nu*1.e-6,2), "Mhz doesn't belongs to this interval\n")


def computeGainDB(A, B, wavelength, eps_ap) :
    return 10*log10(4*pi*eps_ap*A*B/pow(wavelength,2))

def optimal_B(A, a, b) :
    return 0.5*(b + sqrt(b**2 + 8/3*A*(A-a)))

def compute_RH(A,a,wavelength) :
    return A*(A-a)/(3*wavelength)




freq_limits = frequency_limits(a,b, freq_wave)
test_frequency(freq_wave,freq_limits)

B_opti = optimal_B(A, a, b)
R_H = compute_RH(A,a,wavelength)
gain = computeGainDB(A, B_opti, wavelength, 0.51)

print("A =", A*100, "cm\n")
print('The best B from given A, a & b is B =', round(B_opti*1.e2, 2), 'cm\n')
print('R_H = ',round(R_H*1.e2,2), 'cm\n')
print('G =', round(gain,2), 'dB\n')