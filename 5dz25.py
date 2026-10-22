import json
with open("students.json") as f:
    students = json.load(f)
for s in students:
    s["passed"] = s["score"] >= 60
with open("students_out.json", "w") as f:
    json.dump(students, f, indent=4)