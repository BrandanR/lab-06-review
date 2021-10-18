import sys
print("BMI: Body Mass Index Calculator v.0.1 beta")
userWeight = input("Enter your weight (in pounds): ")
userHeight = input("Enter your height (in inches): ")

#myBMI = (703 * float(userWeight)) / (float(userHeight) * float(userHeight))
myBMI = (703 * float(userWeight)) / pow(float(userHeight), 2)
myBMI = round(myBMI, 2)
print("Your body mass index (BMI) is " + str(myBMI) + "%")
