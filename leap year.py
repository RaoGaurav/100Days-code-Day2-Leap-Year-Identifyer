# program to find leap year 
# input year that user want to check
year=int(input("year that you want to search eg.2020 :-"))

# condittion statements
if (year%4==0):
  if (year%100==0):
    if(year%400==0):
      print(f"year {year} ia a leap year")
    else:
      print(f"year {year} is not a leap year")
  else:
    print(f"year {year} ia a  leap year")
else:
  print(f"year {year} ia not a leap year")
input()