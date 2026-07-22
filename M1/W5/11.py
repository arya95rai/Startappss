# 11.
# Group employees according to salary range.
# 0-20000
# 20001-50000
# 50001+
# Use defaultdict.
from collections import defaultdict
d=defaultdict(list)
employees={
    "arya":21000,
    "pehu":50000,
    "prachi":70000,
    "cindy":70000
}
for name,salary in employees.items():
    if salary<=20000 and salary>=0:

        d["0-20000"].append(name)
    elif salary<=50000 and salary>20000:
        d["20001-50000"].append(name)
    else:
        d["50001+"].append(name)
print(dict(d))




