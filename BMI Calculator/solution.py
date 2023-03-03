# BMI Calculator

h = float(input("Enter the height: "))
w = float(input("Enter the weight: "))
w1 = w * 2.20462
h1 = h / 100
print(f"Height is {h1} m")
print(f"Weight is {w} kg")
BMI = w / (h1 * h1)
print("BMI of the person is: ", BMI)
if BMI <= 18.5:
  print("Underweight.\n")
elif BMI > 18.5 and BMI <= 25:
  print("Healthy.\n")
elif BMI > 25.5 and BMI < 30:
  print("Overweight.\n")
else:
  print("Obese.\n")

  

  
