def intersection(arr1,arr2,arr3,l,m,n):
    p=l+m+n
    start1=0
    start2=0
    start3=0
    for i in range(0,p):
        if(arr1[start1]==arr2[start2] and arr1[start1]==arr3[start3]):
             print(arr3[start3])
             start1=start1+1
             start2=start2+1
             start3=start3+1

        elif (arr1[start1]<arr2[start2] and arr1[start1]<arr3[start3] ):
            start1=start1+1
        elif (arr2[start2]<arr1[start1] and arr2[start2]<arr3[start3] ):
            start2=start2+1
        elif (arr3[start3]<arr2[start2] and arr3[start3]<arr1[start1] ):
            start3=start3+1
        if (start1>=l or start2>=m or start3>=n):
            break

        

            
        
arr1=[1, 5, 10, 20, 40, 80]
arr2=[6, 7, 20, 80, 100]
arr3=[3, 4, 15, 20, 30, 70, 80, 120]
l=len(arr1)
m=len(arr2)
n=len(arr3)
intersection(arr1,arr2,arr3,l,m,n)