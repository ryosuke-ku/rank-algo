import csv
from sklearn.metrics import label_ranking_average_precision_score, average_precision_score


with open('smell2.csv','r',encoding = "utf-8-sig") as f:
    # csvをとにかく頭から1行ずつ読み込む
    reader = csv.reader(f)
    map_array = []
    for r in reader:
        # print(r)
        ap_array = []
        for item in r:
            ap_array.append(int(item))
            # print(sum(ap_array))

        if sum(ap_array) == 0:
            ap = 0 
            map_array.append(ap)
        else:
            ap = average_precision_score(ap_array, [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
            map_array.append(ap)
        print(ap_array)
        print('ap:' + str(ap))
    print('map:' + str(sum(map_array)/15))
        # print(r)