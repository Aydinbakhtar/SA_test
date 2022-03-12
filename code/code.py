import math as mt

DELTA = 0.06836475207879
Rn = 2.48352238144356
G = 0.522290322580647
gama = 0.065892450196755
T = 6.89107142857145
u2 = 2.27857952542234
es = 1.05630754978196
ea = 0.841877117176222
Tmin = 1.45
Tmax = 12.3321428571429
RHmean = 79.7






# ET1 = 0.408 * DELTA * (Rn-G)
# ET2 = gama * (900/(T + 273))
# ET3 = u2*(es-ea)
# ET4 = DELTA + gama * (1 + 0.34 * u2)


# print(ET4)
    

PET = (((0.408 * ((2503.06*mt.exp(17.27*(((Tmax+Tmin)/2))/(((Tmax+Tmin)/2)+237.3)))/(((Tmax+Tmin)/2)+237.3)**2) * (Rn-G))) + ((gama) * (900/(((Tmax+Tmin)/2) + 273))) * (u2*(es-((RHmean/100)*((0.6108*mt.exp((17.27*Tmax)/(Tmax+237.3))) + (0.6108*mt.exp((17.27*Tmin)/(Tmin+237.3))))/2)))) / ((((2503.06*mt.exp(17.27*(((Tmax+Tmin)/2))/(((Tmax+Tmin)/2)+237.3)))/(((Tmax+Tmin)/2)+237.3)**2)) + gama * (1 + 0.34 * u2))
    
print(PET)



# delta = ((2503.06*mt.exp(17.27*(((Tmax+Tmin)/2))/(((Tmax+Tmin)/2)+237.3)))/(((Tmax+Tmin)/2)+237.3)**2)

# print(delta)



