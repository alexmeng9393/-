tall=float(input())
weight=float(input())
tallm=tall/100
BMI=round((weight/tallm**2),2)
print(BMI)
if BMI <18.5:
    print("Underweight")
elif 18.5<=BMI<24 :
    print("Normal")
elif 24<=BMI<27:
    print("Overweight ")
elif 27<=BMI<30 :
    print("Obese Class I")
elif 30<=BMI<35  :
    print("Obese Class II")
elif BMI>=35 :
    print("Obese Class III ")


