from collections import Counter, deque, defaultdict

# Count log levels
log_counter = Counter()

# Store latest 20 logs
latest_logs = deque(maxlen=20)

# Group logs by date
logs_by_date = defaultdict(list)

with open("log.txt", "r") as file:
    for line in file:
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        parts = line.split(maxsplit=2)

        date = parts[0]
        level = parts[1]

        # Counter
        log_counter[level] += 1

        # Latest 20 logs
        latest_logs.append(line)

        # Group by date
        logs_by_date[date].append(line)


# ---------------- Output ----------------

print("ERROR Count :", log_counter["ERROR"])
print("INFO Count :", log_counter["INFO"])
print("WARNING Count :", log_counter["WARNING"])

print("\nLatest 20 Logs")
for log in latest_logs:
    print(log)

print("\nLogs Grouped Date-wise")

for date, logs in logs_by_date.items():
    print(date)
    for log in logs:
        print(" ", log)