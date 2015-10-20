def weather_info (temp):
    c = convertToCelsius(temp)
    if (c <= 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
    
def convertToCelsius (temp):
  temp = (((float(temp) - 32) * 5) / 9)
  return temp
