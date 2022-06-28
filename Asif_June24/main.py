'''first_name = 'Asif'
print(first_name)
last_name = 'Ahmad'
print(last_name)
full_name = first_name+' '+last_name
print(full_name)
print(full_name.title())
print(full_name.upper())
print(full_name.lower())

print('For White Space adding & removing\n')
New_Name = '  Asif Ahmad  '
print(New_Name)
print(New_Name.lstrip())
print(New_Name.rstrip())
print(New_Name.strip())
print('\n')

print('Hi Guys')
Weight = float(input('Enter your weight in KG:\t'))
Height = float(input("Enter your height in Feet\t"))

Height_in_meter = Height / 3.28

BMI = Weight / (Height_in_meter)**2
print('Your Body mass index is',BMI)

if BMI <= 18.5:
    print('Oops! You are underweight.')
elif BMI <=24.9:
    print('Awesome! You are healthy.')
elif BMI <=29.9:
    print('You are overweight.')
else:
    print('You are obese.')

Number = int(input('Enter a number: '))
fact = 1.0
for i in range(1, Number+1):
    fact = fact*i
print('The factorial of',Number, 'is',fact)
#print((2**31)-1)
print(5//4)
print(5/4)


#Farheneight to Celsius
Input_for_Fareneight = float(input('Enter Temprature in farheneight: '))
Celsius = (Input_for_Fareneight-32)/(9/5)
temprature_celsius = round (Celsius,3)
print('Temprature in Celsius is: ',temprature_celsius)

#Celsius to Farheneight
Input_for_Celsius = float(input('Enter Temprature in Celsius: '))
Farheneight = Input_for_Celsius*(9/5)+32
temprature_farheneight = round(Farheneight,3)
print('Temprature in Farheneight is: ',temprature_farheneight)

# Farheneight to Celsius and Celsius to Farheneight

User = eval(input('Press 1 for Farheneight to Celsius or 2 for Celsius to Farheneight: '))

if User == 1:
    Input_for_Fareneight = float(input('Enter Temprature in farheneight: '))
    Celsius = (Input_for_Fareneight-32)/(9/5)
    temprature_celsius = round (Celsius,3)
    print('Temprature in Celsius is: ',temprature_celsius)

elif User == 2:
    Input_for_Celsius = float(input('Enter Temprature in Celsius: '))
    Farheneight = Input_for_Celsius*(9/5)+32
    temprature_farheneight = round(Farheneight,3)
    print('Temprature in Farheneight is: ',temprature_farheneight)

else:
    print('Invalid Input Try Again')'''

# Distance from Km to Miles and Miles to KM

User = eval(input('Press 1 for Kilometer to Miles or 2 for Miles to KM: '))

if User.isdigit():
    print('Enter a valid input')
elif User == 1:
    Input_in_KM = float(input('Enter Distance in KM: '))
    Distance_in_Miles = (Input_in_KM/0.62)
    For_Round_Off = round(Distance_in_Miles,3)
    print('Distance in miles is: ',For_Round_Off)

elif User == 2:
    Input_in_Miles = float(input('Enter Distance in Miles: '))
    Distance_in_Km = Input_in_Miles*0.62
    For_Round_Off = round(Distance_in_Km)
    print('Distance in kilometer is: ',For_Round_Off)
else:
    print('Invalid Input, Try Again')

