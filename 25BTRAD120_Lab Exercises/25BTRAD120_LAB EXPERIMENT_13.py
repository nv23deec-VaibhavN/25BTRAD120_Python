import csv
INPUT_FILE = "employees. csv"
# Sample employee data: Basic salary, HRA and DA.
sample_employees = [
{"Emp ID": "E101", "Name": "Ananya", "Basic": "3000",
"HRA": "6000", "DA": "3000"},
{"Emp ID": "E102", "Name": "Rahul", "Basic": "40000",
"HRA": "8000", "DA": "4000"},
{"Emp ID": "E103", "Name": "Meera","Basic": "25000",
"HRA": "5000", "DA": "2500"}
  }
with open(INPUT FILE, "w", newline="", encoding="utf-8") as f:
writer = csv.DictWriter(
f, fieldnames=["Emp ID", "Name", "Basic", "HRA", "DA"]

)

writer.writeheader()
writer.writerows (sample_employees)
total_gross = 0
total_deduction = 0
total_net = 0
print("PAYROLL SUMMARY")
print(" -" * 75)
print(f'{"ID" :< 8}{"NAME" :< 12}{"GROSS":>12}{"DEDUCTION":>15}{"NET SALARY":>15}')
print("-" * 75)
with open(INPUT_FILE, "r", newline="", encoding="utf-8") as f:
reader = csv.DictReader(f)
for emp in reader:
try:
basic = float(emp["Basic"]
hra = float(emp["HRA"])
da = float (emp["DA"])
if min(basic, hra, da)<0:
raise ValueError
gross = basic + hra + da
pf = basic * 0.12

# PF = 12% of basic salary

tax = gross * 0.05

# Tax = 5% of gross salary
deduction = pf + tax
net = gross - deduction
total_gross += gross
total_deduction += deduction
total_net += net
print(f' {emp["Emp ID"] :< 8}{emp["Name"] :< 12}'
f'{gross:>12.2f}{deduction:>15.2f} {net:>15.2f} ')
except (ValueError, TypeError) :
print(f' Invalid salary data for {emp["Emp ID"]}')
print("-" * 75)
print(f"Total Gross Salary : Rs. {total_gross :. 2f}")
print(f"Total Deductions
: Rs. {total_deduction: .2f}")
print(f"Total Net Salary
: Rs. {total_net :. 2f}")
