Rent=int(input("Enter your rent of hostel/flat:"))
Food=int(input("Enter the amount of food ordered:"))
Electricity_spend=int(input("Enter the total electricity spend in unit:"))
Charge_per_unit=int(input("Enter the charge per unit:"))
Cleaning_cost=int(input("Enter the cleaning cost:"))
Persons=int(input("Enter the no of persons living in the hostel/flat:"))
Total_bill=Electricity_spend*Charge_per_unit
Output=(Rent+Food+Cleaning_cost+Total_bill)//Persons
print(f"Each person will pay rs {Output}")
