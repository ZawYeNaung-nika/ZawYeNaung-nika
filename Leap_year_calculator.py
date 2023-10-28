year_check = int(input("Enter the year : "))

if (year_check % 4 == 0 and year_check % 100 != 0) or year_check % 400 ==0:
    print(f'{year_check} is a leap year')
else:
          print(f'{year_check} is not leap year')