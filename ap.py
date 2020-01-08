from sklearn.metrics import label_ranking_average_precision_score, average_precision_score
average_precision_score([1, 0, 1, 0], [1, 0.8, 0.6, 0.4], average='samples')
#0.79166666666666663
label_ranking_average_precision_score([[1, 0, 1, 0]], [[1, 0.8, 0.6, 0.4]])
#0.83333333333333326