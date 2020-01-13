from sklearn.metrics import label_ranking_average_precision_score, average_precision_score

a1 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(a1)

b1 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(b1)

c1 = average_precision_score([1,1,1,1,1,1,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
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

j1 = average_precision_score([1,1,1,1,1,1,1,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(j1)

k1 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(k1)

l1 = average_precision_score([1,1,1,1,1,1,0,0,0,1], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(l1)

m1 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(m1)

n1 = average_precision_score([0,0,0,0,0,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(n1)

O1 = average_precision_score([1,1,0,0,0,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(O1)

map = (a1+b1+c1+d1+e1+f1+g1+h1+i1+j1+k1+l1+m1+n1+O1)/15
print("map1: " + str(map))


a2 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(a2)

b2 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(b2)

c2 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(c2)

d2 = average_precision_score([1,1,1,1,0,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(d2)

e2 = average_precision_score([1,1,1,1,0,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(e2)

f2 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(f2)

g2 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(g2)

h2 = average_precision_score([1,1,1,1,1,1,0,0,1,1], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(h2)

i2 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(i2)

j2 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(j2)

k2 = average_precision_score([1,1,1,1,1,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(k2)

l2 = average_precision_score([1,1,1,1,1,1,1,1,1,1], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(l2)

m2 = average_precision_score([1,1,1,1,1,1,0,0,1,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(m2)

n2 = average_precision_score([1,1,0,1,0,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(n2)

O2 = average_precision_score([1,1,1,1,0,0,0,0,0,0], [1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1], average='samples')
print(O2)


map2 = (a2+b2+c2+d2+e2+f2+g2+h2+i2+j2+k2+l2+m2+n2+O2)/15
print("map2: " + str(map2))

#label_ranking_average_precision_score([[1, 0, 1, 0]], [[1, 0.8, 0.6, 0.4]])
#0.83333333333333326