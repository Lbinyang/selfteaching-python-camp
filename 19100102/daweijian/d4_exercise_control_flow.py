#-----------------------------------------------
#今日份作业：

#以下代码摘自：博客“疯狂的小可乐“
#-----------------------------------------------

print("1.使用for in 循环打印九九乘法表")
for i in range(1,10):
    for j in range(1,i+1):
        d = i * j
        print('%d×%d=%-2d'%(i,j,d),end = ' ' )
    print()

print("2.使用while循环打印九九乘法表并用条件判断把偶数行去掉")
i=1
while i <= 9:
    j = 1
    while j <= i and i%2!=0:
        print("%d×%d=%-2d"%(i,j,i*j),end = ' ')  # %d： 整数的占位符，'-2'代表靠左对齐，两个占位符
        j += 1
    print()
    i += 1
