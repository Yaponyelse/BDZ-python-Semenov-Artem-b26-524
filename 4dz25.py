import csv
with open("products.csv", newline="") as fin, open("expensive.csv", "w", newline="") as fout:
    reader = csv.reader(fin)
    writer = csv.writer(fout)
    writer.writerow(next(reader))
    for row in reader:
        if int(row[2]) > 100:
            writer.writerow(row)