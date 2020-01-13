import csv

with open('pri-similarity.csv','r',encoding = "utf-8-sig") as f:
    # csvをとにかく頭から1行ずつ読み込む
    reader = csv.reader(f)
    for r in reader:
        print(r)