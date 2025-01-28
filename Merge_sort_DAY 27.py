def merg_sort(arr,l,r):
    mid=(r+l)/2
    if l <= r:
        return
    merg_sort(arr , l, mid)
    merg_sort(arr , mid+1 , r)
    merg(arr  , l , mid , r)
def merg(arr , l , mid , r):
    lft=l
    rgt=mid-1
    k = 0
    while(lft <= mid and rgt < r):
        if arr[lft] <= arr[rgt]:
            arr[k]=arr[lft]
            k +=1
            lft +=1
        else:
            arr[k] = arr[rgt]
            k += 1
            rgt += 1
        while(lft <= mid):
            arr[ k ] = arr[lft]
            k += 1
            lft += 1
        while(rgt <= r):
            arr[k] =arr[rgt]
            k +=1
            rgt +=1

arr=[2 , 4 , 5 ,7 ,8]
l=0
r=len(arr)
merg_sort(arr,l,r)
print(arr)