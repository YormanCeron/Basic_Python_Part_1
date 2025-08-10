#Exercise 1: Calculate the arithmetic mean of two numbers

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = (a+b)/2
print("The arithmethic mean is:", c)

#Exersice 2: convert Celsius to Fahrenheit

c = float(input("Enter the temperature in degrees celsius: "))
f = (1.8 * c) + 32
print("The temperature in degrees Fahrenheit is:", f,"F")


#Exercise 3: Convert Fahrenheit to Celsius
f = float(input("Enter the temperature in degrees Fahrenheit: "))
c = (f-32)/1.8
print("The temperature in degrees Celsius is:", c,"ºC")

#Exercise 4: Calculate the number of minutes and seconds from a given number of seconds 
cant_s = float(input("Enter the seconds: "))
m = int(cant_s/60)
s = round(((cant_s/60) - m) * 60, 2)
print(m)
print(s)

cant_s = float(input("Enter the seconds: "))
m = int(cant_s/60)
s = cant_s%60
print(m)
print(s)

#Exercise 5: Convert seconds to hours, minutes, and seconds
cant_s = float(input("Enter the seconds: "))
h = int(cant_s/3600)
m = int(((cant_s/3600) - h)*60)
s = int(((((cant_s/3600) - h)*60)-m)*60)
print(h)
print(m)
print(s)