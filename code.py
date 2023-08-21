from ipywidgets import interactive

#Define
f1 = 2 #focus lens 1
f2 = 3 #focus lens 2


def fx(o1,L):
  #calculation
  i1 = (o1*f1)/(o1-f1) #image lens 1
  o2 = L-i1            #object lens 2
  i2 = (o2*f2)/(o2-f2) #image lens 2
  M1 = i1/o1           #magnification of lens 1
  M2 = i2/o2           #magnification of lens 2
  Mtot = M1*M2         #overall magnification
  
  #result
  print("Distance object for first lens, I2 :", o1, "cm")
  print("Distance object for second lens, I2 :", o2, "cm")
  print("Distance image for first lens, I1 :", i1, "cm")
  print("Distance image for second lens, I2 :", i2, "cm")
  print("Magnification of first lens, M1 : ", M1)
  print("Magnification of second lens, M2 : ", M2)
  print("Overall magnification, Mtot : ", Mtot)

#slider
interactive(fx, o1=(0.1,5,0.01), L=(0.1,10,0.01))
