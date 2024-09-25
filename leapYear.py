# check weather the year is a leap year or not
#Lwazi somtsewu
#31 jULY 2024
year= int(input("Enter a year:\n"))

leapyear = year % 4==0
leapyear = leapyear and ((year % 100)!= 0)
leapyear = leapyear or ((year % 400)== 0)

if leapyear == True:
    print( year ,"is a leap year.")

else:
    print( year ,"is not a leap year.")