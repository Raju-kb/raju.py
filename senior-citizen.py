from datetime import date
pername=input("Enter the name of the person :")
perDOB= int(input("Enter his year of birth :"))
curYear=date.today().year
perAge=curYear-perDOB
if (perAge>60):
    print(pername,"aged",perAge,"years is a senior citizen.")
else:
    print(pername,"aged",perAge,"years is not a senior citizen")
