import csv
total = 0
count = 0
best_name = None
best_score = None
group_sum = {}
group_cnt = {}
with open("students.csv", newline="") as f:
    for row in csv.DictReader(f):
        score = int(row["score"])
        group = row["group"]
        total += score
        count += 1
        if best_score is None or score > best_score:
            best_score = score
            best_name = row["name"]
        group_sum[group] = group_sum.get(group, 0) + score
        group_cnt[group] = group_cnt.get(group, 0) + 1
print(total / count)
print(best_name)
for g in group_sum:
    print(f"{g} {group_sum[g] / group_cnt[g]}")