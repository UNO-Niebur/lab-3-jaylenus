#TempConvert.py
#Name: Jaylen Atsou
#Date: Feburary 7, 2026
#Assignment: Lab 3

def main():
  tempF = int(input("Enter a Fahrenheit temperature: "))

  tempC = (tempF - 32)*5/9
  tempCRounded = round(tempC, 1)

  print(tempF, "is ", tempCRounded, "degrees celsius.")
  
if __name__ == '__main__':
  main()
