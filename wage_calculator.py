# Salary calculation script for daily wage workers based on tonnage

# Initialize dictionaries and variables
salary = {}
salary_detail = {}
total_money = 0
total_tonnage = 0
day = 0

# Continue until the user decides to stop
while input("Do you want to continue? (y/n) ").lower() != "n":
    day += 1
    print("\nDay", day)

    # Get the tonnage and calculate the amount for the day
    tonnage = float(input("Enter Tonnage: "))
    total_tonnage += tonnage
    daily_total = tonnage * 700  # Assuming 700 is the rate per ton

    # Get the number of workers and calculate individual wages
    total_workers = int(input("Enter Number of Workers: "))
    wage_per_worker = daily_total / total_workers
    print("Calculated wage per worker: ", wage_per_worker)

    # Adjust the wage based on user input if needed
    wage = float(input("Enter actual wage per worker (or press Enter to use calculated wage): ") or wage_per_worker)

    # Collect salary details for each worker
    for i in range(total_workers):
        name = input(f"Enter Name of Worker {i+1}: ")

        # Update total salary for each worker
        salary[name] = salary.get(name, 0) + wage

        # Update total money distributed
        total_money += wage

        # Maintain detailed records for each worker
        if name not in salary_detail:
            salary_detail[name] = [wage]
        else:
            salary_detail[name].append(wage)

    # Print separator
    print("-" * 100)

    # Print daily summary
    print("\n" * 2)

# Print the overall summary
print("Summary of Payments")
print("-" * 100)
c = 1
for name, total_salary in salary.items():
    days_worked = len(salary_detail[name])
    wage_history = salary_detail[name]
    print(f"{c}) {name} = {total_salary:.2f}, Days: {days_worked}, Wages per day: {wage_history}")
    c += 1

print("\nTotal Money Distributed: ", total_money)
print("Total Tonnage Processed: ", total_tonnage)

print("\n" * 2)
