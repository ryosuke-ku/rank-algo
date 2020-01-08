from sklearn.metrics import label_ranking_average_precision_score, average_precision_score
a1 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(a1)

b1 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(b1)

c1 = average_precision_score([1,1,1,1,1,0,1,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(c1)

d1 = average_precision_score([1,1,0,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(d1)

e1 = average_precision_score([1,1,0,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(e1)

f1 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(f1)

g1 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(g1)

h1 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(h1)

i1 = average_precision_score([0,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(i1)

j1 = average_precision_score([1,1,1,1,1,0,1,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(j1)

k1 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(k1)

l1 = average_precision_score([1,1,1,1,1,0,1,0,0,1], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(l1)

m1 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(m1)

map = (a1+b1+c1+d1+e1+f1+g1+h1+i1+j1+k1+l1+m1)/13
print("map: " + str(map))

#label_ranking_average_precision_score([[1, 0, 1, 0]], [[1, 0.8, 0.6, 0.4]])
#0.83333333333333326