import csv
from sklearn.metrics import label_ranking_average_precision_score, average_precision_score


with open('smell2.csv','r',encoding = "utf-8-sig") as f:
    # csvをとにかく頭から1行ずつ読み込む
    reader = csv.reader(f)
    map_array = []
    top1 = []
    top2 = []
    top3 = []
    top4 = []
    top5 = []
    top6 = []
    top7 = []
    top8 = []
    top9 = []
    top10 = []

    for r in reader:
        # print(r)
        ap_array = []
        for item in r:
            ap_array.append(int(item))
        print(ap_array)

        cnt = 0
        for val in ap_array:
            if val == 1:
                cnt+=1
        print('cnt:' + str(cnt))

        recall = 0
        num = 0
        top = 0 
        for val in ap_array:
            top += 1 
            num += val
            if num == 0:
                pass
            else:
                recall = num/cnt
            print('top' + str(top) + ':' + str(recall))

            if top == 1:
                top1.append(recall)
            elif top == 2:
                top2.append(recall)            
            elif top == 3:
                top3.append(recall)
            elif top == 4:
                top4.append(recall)            
            elif top == 5:
                top5.append(recall)
            elif top == 6:
                top6.append(recall)            
            elif top == 7:
                top7.append(recall)
            elif top == 8:
                top8.append(recall)            
            elif top == 9:
                top9.append(recall)
            elif top == 10:
                top10.append(recall)

    print('---RESULT---')
    # print(top1)
    print('recall-top1:' + str(round(sum(top1)/len(top1)*100, 1)))
    # print(top2)
    print('recall-top2:' + str(round(sum(top2)/len(top2)*100, 1)))
    # print(top3)
    print('recall-top3:' + str(round(sum(top3)/len(top3)*100, 1)))
    # print(top4)
    print('recall-top4:' + str(round(sum(top4)/len(top4)*100, 1)))
    # print(top5)
    print('recall-top5:' + str(round(sum(top5)/len(top5)*100, 1)))
    # print(top6)
    print('recall-top6:' + str(round(sum(top6)/len(top6)*100, 1)))
    # print(top7)
    print('recall-top7:' + str(round(sum(top7)/len(top7)*100, 1)))
    # print(top8)
    print('recall-top8:' + str(round(sum(top8)/len(top8)*100, 1)))
    # print(top9)
    print('recall-top9:' + str(round(sum(top9)/len(top9)*100, 1)))
    # print(top10)
    print('recall-top10:' + str(round(sum(top10)/len(top10)*100, 1)))
