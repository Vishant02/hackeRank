if __name__ == '__main__':
    i=0
    n = int(input())
    arr = (map(int, input().split()))
    x=sorted(list(arr))
    if n>=2 and n<=10:
        for i in arr:
            if i <=100 and i>=-100:
                i=0
            else:
                i=1
        if i==0:
            while(i==0):
                if x[n-1] > x[n-2]:
                    print(x[n-2])
                    i=1
                else:
                    n-=1a
