import csv
from sklearn.metrics import label_ranking_average_precision_score, average_precision_score


with open('pri-similarity.csv','r',encoding = "utf-8-sig") as f:
    # csvをとにかく頭から1行ずつ読み込む
    reader = csv.reader(f)
    
    for r in reader:
        print(r)
        ap_array = []
        for item in r:
            ap_array.append(int(item))
        ap = average_precision_score(ap_array, [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
        print(ap_array)
        print(ap)
        # print(r)