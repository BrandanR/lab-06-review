tempincelsius = input("Please enter a temperature in celsius ")
tempincelsius = float(tempincelsius)

tempinfahrenheit = tempincelsius * 1.8 + 32
tempinfahrenheit = round(tempinfahrenheit, 2)
print(str(tempincelsius) + " degress Celsius is " + str(tempinfahrenheit) + "°F")
