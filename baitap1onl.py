#Viet ham tinh toan ma tran: nhan ma tran,ham cong ma tran,ham chuyen vi ma tran
X=[[12,7,5],
   [5,-8,9],
   [0,-9,5]]
Y=[[5,-6,0],
   [-1,-8,0],
   [-6,7,8]]
#cong 2 ma tran
sum_X_Y = [[0,0,0],
           [0,0,0],
           [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        sum_X_Y[i][j]=X[i][j]+Y[i][j]
    for k in sum_X_Y:
        print(k)
#nhan 2 ma tran
tich_X_Y = [[0,0,0],
           [0,0,0],
           [0,0,0]]   
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            tich_X_Y[i][j]=X[i][j]*Y[i][j]
for t in tich_X_Y:
    print(t)
#ma tran chuyen vi
mt_cv = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
       mt_cv[j][i] =X[i][j]
for c in mt_cv:
    print(c)
