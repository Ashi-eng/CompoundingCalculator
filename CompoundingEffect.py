money = int(input("Enter the Money given to you on first day: "))
multiplier = int(input("How does the money increment each day?(Doubles/tribles etc ): " ))#Enter in numbers
days = int(input("Enter the Days: "))

unit_for_days = []
unit_for_days.append(1)

for i in range(1,days):
    unit_for_days.append(unit_for_days[i-1] * multiplier) #Genearting the list of numbers for 1 unit after incrementing everyday for multiplier times

print(f"Total money compounded for {days} days is {sum(unit_for_days) * money} ")
