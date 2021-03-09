from math import pi, log10, sqrt
import numpy as np
import matplotlib.pyplot as plt

# Setting constants
lightspeed = 3.0e8
eps_ap = 0.51

def plotLength(x1,y1,x2,y2, label, side, color ="black") :
    #Plot double arrow
    plt.arrow(x1,y1,x2-x1,y2-y1, length_includes_head=True, head_width = 2, color=color, alpha=0.5)
    plt.arrow(x2,y2,x1-x2,y1-y2, length_includes_head=True, head_width = 2, color=color, alpha=0.5)

    #Plot text label on good side
    if side=="North" :
        plt.text((x2+x1)/2 - 4, y1+1, label)
    elif side == "South" :
        plt.text((x2+x1)/2 - 4, y1-4, label)
    elif side == "East" :
        plt.text(x1+1, (y2+y1)/2 - 1, label)
    elif side == "West" :
        plt.text(x1-9, (y2+y1)/2 - 1, label)

class Horn() :
    def __init__(self, A,a,b,c) :
        self.A = A
        self.a = a
        self.b = b
        self.c = c
        self.compute_carac()

    def __str__(self) :
        return self.affiche()
    
    def compute_carac(self) :
        self.B = 0.5*(self.b + sqrt(self.b**2 + 8/3*self.A*(self.A-self.a)))
        self.R_H = self.A*(self.A-self.a)/(3*wavelength)
        self.L_A = sqrt(self.R_H**2 + ((self.B-self.b)/2)**2)
        self.L_B = sqrt(self.R_H**2 + ((self.A-self.a)/2)**2)

        self.Gain = 10*log10(4*pi*eps_ap*self.A*self.B/pow(wavelength,2))

    def test_frequency(self) :
        lambda_c = 2*self.a 
        nu_c = lightspeed/lambda_c
        nu_min = 1.25*nu_c
        nu_max = 1.9*nu_c
        print("The horn frequency limits are : ", round(nu_min*1.e-6,2), "Mhz < nu < ",  round(nu_max*1.e-6,2), "Mhz")
        if nu_min<freq_wave<nu_max :
            print("Your frequency nu =", round(freq_wave*1.e-6,2), "Mhz is OK with those a and b\n")
        else :
            print("Your frequency nu =", round(freq_wave*1.e-6,2), "Mhz doesn't belongs to this interval\n")

    def affiche(self) :
        attr = ["A", "B", "a", "b", "c", "L_A", "L_B", "R_H", "Gain"]
        form = "{0:12}{1:12}{2:12}{3:12}{4:12}{5:12}{6:12}{7:12}{8:12}"
        carac = [str(round(100*self.A,2)), str(round(100*self.B,2)), str(round(100*self.a,2)), str(round(100*self.b,2)), str(round(100*self.c,2)), str(round(100*self.L_A,2)), str(round(100*self.L_B,2)), str(round(100*self.R_H,2)), str(round(self.Gain,2))]
        
        return("Characteristics of the GalaxyClock : \n" + form.format(*attr)+"\n"+ form.format(*carac))

    def generePlan(self, woodplanksize) :
        color_A = "#7319CD"
        color_B = "#FFAE00"
        color_a = "#00FFBD"
        color_b = "#0080FF"
        color_c = "#C900FF"

        x_p, y_p = woodplanksize
        fig = plt.figure(figsize=[12.,6.])
        plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')
        plt.xlim(-30,x_p+50)

        #Plotting the wooden plank and its dimensions
        plt.plot([0, 0, x_p, x_p, 0],[0, y_p, y_p, 0, 0], color="black", linestyle="dashed", alpha = 0.5) #Plank dimensions
        plt.plot([(x_p-100*self.c)/2, (x_p-100*self.c)/2],[0, y_p], color="black", linestyle="dashed", alpha = 0.5) #Half plank when you remove the right reclangle where box part are cut
        plotLength(-4, 0, -4, y_p, str(y_p), "West")
        plotLength(0,-4,x_p,-4, str(x_p), "South")

        #Plotting A trapeze and its dimensions
        x_trapeze_A = np.array([0, 0, self.L_A, self.L_A, 0])*100
        y_trapeze_A = np.array([0, self.A, (self.A + self.a)/2, (self.A - self.a)/2, 0])*100
        plt.plot(x_trapeze_A, y_trapeze_A, color=color_A, label="Planck A")
        plotLength(2,0, 2, 100*self.A, str(round(100*self.A,1)), "East", color_A)
        plotLength(100*self.L_A-2, 100*(self.A - self.a)/2, 100*self.L_A-2, 100*(self.A + self.a)/2, str(100*self.a), "West", color_A)
        plotLength(0, -8, 100*self.L_A, -8, str(round(100*self.L_A,1)), "South", color_A)

        #Plotting B trapeze and its dimensions
        x_trapeze_B = np.array([self.L_B, self.L_B, 0, 0, self.L_B])*100 + (x_p-100*self.c)/2 - 100*self.L_B
        y_trapeze_B = np.array([y_p/100, y_p/100 - self.B, y_p/100 - (self.B + self.b)/2, y_p/100 - (self.B - self.b)/2, y_p/100])*100
        plt.plot(x_trapeze_B, y_trapeze_B, color=color_B, label="Planck B")
        plotLength((x_p-100*self.c)/2 - 100*self.L_B + 2, y_p - (100*self.B + 100*self.b)/2, (x_p-100*self.c)/2 - 100*self.L_B + 2, y_p - (100*self.B - 100*self.b)/2, str(100*self.b), "East", color_B)
        plotLength((x_p-100*self.c)/2 - 2, y_p-100*self.B, (x_p-100*self.c)/2 - 2, y_p, str(round(100*self.B,1)), "West", color_B)
        plotLength((x_p-100*self.c)/2 - 100*self.L_B, y_p + 4, (x_p-100*self.c)/2, y_p + 4, str(round(100*self.L_B,1)), "North", color_B)

        #Plotting Box rectangles and their dimentions
        plt.plot([x_p-100*self.c, x_p-100*self.c],[0, y_p], color="black", linestyle="dashed", alpha = 0.5) #Right reclangle where box part are cut
        plt.plot([x_p-100*self.c, x_p, x_p, x_p-100*self.c, x_p-100*self.c], [y_p, y_p, y_p-100*self.a, y_p-100*self.a, y_p],color=color_a, label="Plank a")
        plt.plot([x_p-100*self.c, x_p, x_p, x_p-100*self.c, x_p-100*self.c], [y_p-100*self.a, y_p-100*self.a, y_p-100*2*self.a, y_p-100*2*self.a, y_p-100*self.a],color=color_a)
        plt.plot([x_p-100*self.c, x_p, x_p, x_p-100*self.c, x_p-100*self.c], [y_p-100*2*self.a, y_p-100*2*self.a, y_p-100*(2*self.a+self.b), y_p-100*(2*self.a+self.b), y_p-100*2*self.a],color=color_b, label="Plank b")
        plt.plot([x_p-100*self.c, x_p, x_p, x_p-100*self.c, x_p-100*self.c], [y_p-100*(2*self.a+self.b), y_p-100*(2*self.a+self.b), y_p-100*(2*self.a+2*self.b), y_p-100*(2*self.a+2*self.b), y_p-100*(2*self.a+self.b)],color=color_b)
        plt.plot([x_p-100*self.c, x_p-100*(self.c-self.b), x_p-100*(self.c-self.b), x_p-100*self.c, x_p-100*self.c], [y_p-100*(2*self.a+2*self.b), y_p-100*(2*self.a+2*self.b), y_p-100*(3*self.a+2*self.b), y_p-100*(3*self.a+2*self.b), y_p-100*(2*self.a+2*self.b)],color=color_c, label="Plank c")
        plotLength(x_p-100*self.c, y_p+2 , x_p, y_p+2, str(round(100*self.c,1)), "North", color_a)
        plotLength(x_p+2, y_p-100*self.a, x_p+2, y_p, str(round(100*self.a,1)), "East", color_a)
        plotLength(x_p+2, y_p-100*2*self.a, x_p+2, y_p-100*self.a, str(round(100*self.a,1)), "East", color_a)
        plotLength(x_p+2, y_p-100*(2*self.a+self.b), x_p+2, y_p-100*2*self.a, str(round(100*self.b,1)), "East", color_b)
        plotLength(x_p+2, y_p-100*(2*self.a+2*self.b), x_p+2, y_p-100*(2*self.a+self.b), str(round(100*self.b,1)), "East", color_b)
        plotLength(x_p+2, y_p-100*(3*self.a+2*self.b), x_p + 2, y_p-100*(2*self.a+2*self.b), str(round(100*self.a,1)), "East", color_c)
        plotLength(x_p-100*self.c, y_p-100*(3*self.a+2*self.b)-2 , x_p-100*(self.c-self.b), y_p-100*(3*self.a+2*self.b)-2, str(round(100*self.b,1)), "South", color_c)

        plt.title("Cutting plan of wooden board (lengths are in cm)")
        plt.legend(loc="lower right")
        plt.show()

#Wave caracteristics
freq_wave = 1.4204e9
wavelength = lightspeed/freq_wave

#Parameters of the horn (in m)
a = 16.3e-2
b = 10.5e-2
c = 15.0e-2
A = 56.6e-2

Galacticlock = Horn(A,a,b,c)
Galacticlock.test_frequency()
print(Galacticlock)
Galacticlock.generePlan([160.0,80.0])