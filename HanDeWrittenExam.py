def implea():
    a=[]
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    '''
                    if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
                    '''
                    a.append((i,j,k,l))
    return a
def test(nums,x,y):
    a=implea()
    for i in a:
        j=0
        print(i)
        count=0
        while j<6:
            count1=0
            count2=0
            for k in range(4):
                if i[k]==int(nums[j][k]):
                    count1+=1
            for m in range(4):
                for n in range(4):
                    if i[m]==int(nums[j][n]) and m!=n:
                        count2+=1
            if count1!=x[j] or count2!=y[j]:
                break
            j=j+1
            count=count+1
            if count==6:
                return i
    return "sorry"
def main():
    nums=['2940','8592','7468','2691','2379','6035']
    x=[1,0,0,1,1,0]
    y=[1,2,1,1,0,1]
    result=test(nums,x,y)
    print(result)
if __name__=='__main__':
    main()

