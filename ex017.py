from math import hypot

cat_op = float(input('qual o comprimento do cateto oposto?'))
cat_adj = float(input('qual o comprimento do cateto adjacente? '))
hipo = hypot(cat_op, cat_adj)
print('a hipitenusa vale {:.2f}'.format(hipo))