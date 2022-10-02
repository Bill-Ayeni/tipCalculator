print("Welcome to the tip calculator")
bill = float(input("What was the bill "))
peop = int(input("How many people "))
per = (input("What percentage tip? 10, 12, 15 "))

if per == "10":
    Total = (bill*1.1)/peop
    print(Total)

elif per == "12":
    Total = (bill*1.12)/peop
    print(Total)

else:
    Total = (bill*1.15)/peop
    print(Total)
