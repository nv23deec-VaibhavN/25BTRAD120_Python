from pathlib import Path
def analyse_log(filename) :
path = Path (filename)
if not path.exists():
print("Error: Log file not found. ")
returr
if path.stat().st_size == 0:
print("The log file is empty.")
return
counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}
with path.open("r", encoding="utf-8") as file:
for line in file:
for keyword in counts:
if keyword in line.upper():
counts[keyword] += 1
break
print("\nLOG FILE SUMMARY")
print(" -.
for keyword, count in counts.items():
print(f"{keyword} : {count}")
# Create a sample application log for demonstration.
sample_logs = [
"INFO: Application started",
"WARNING: Low disk space",
"ERROR: Unable to connect to database",
"INFO: User logged in",
"ERROR: Invalid file format"
"WARNING: High memory usage"
with open("application. log", "w", encoding="utf-8") as file:
file.write("\n".join(sample_logs))
analyse_log("application. log")
analyse_log("application. log")
