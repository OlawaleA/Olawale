def CeltoFar(celsius):
   return celsius * (9.0/5) + 32

i = float(raw_input("enter a value to change celsius to farenheit"))
F= CeltoFar(i)
print 'temperature in Far is :', F

def FartoKel (farenheit):
    return ((farenheit - 32) * (5.0/9)) + 273.15

K= FartoKel(F)
print 'temperature in Kel is :', K

def KeltoCel(kelvin):
    return kelvin - 273.15

C= KeltoCel(K)
print 'temperature in Far is :', C
