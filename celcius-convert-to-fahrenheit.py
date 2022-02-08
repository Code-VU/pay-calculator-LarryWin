def convertCelciusToFahrenheit():
    sCelcius = input("Enter temperature in Celcius: ")
    fCelcius = float(sCelcius)
    fFahrenheit = (fCelcius * (9/5)) + 32
    fCelcius = "{:.10f}".format(fCelcius)
    fFahrenheit = "{:.2f}".format(fFahrenheit)
    print("The temperature", fCelcius, "in Celcius is", fFahrenheit, "in Fahrenheit")

convertCelciusToFahrenheit()