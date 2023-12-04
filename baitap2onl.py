#Viet ham nhap ma tran (mxn) va ham in ra noi dung ma tran (mxn) ra man hinh 
#nhap ma tran
a=[]
m=int(input("nhap m la:"))
n=int(input("nhap n la:"))
for i in range(m):
    print("nhap ma tran hang thu",i+1, ": ")
    b=[]
    for j in range(n):
        x=int(input("nhap phan tu thu "+str(j+1)+": "))
        b=b+[x]
    a.append(b)
    print("ma tran vua nhap co dang la:")
# in ra man hinh ma tran
for i in range(m):
    for j in range(n):
        print(a[i][j], end=" ")
    print()


