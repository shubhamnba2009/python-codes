t=int(raw_input())
def bin_sea(arr,l,h,key):
    if(l>h):
        return -1
    mid=(l+h)/2
    if(arr[mid]==key):
        return mid
    
    if(arr[l]<=arr[mid]):
        if(key>=arr[l] and key<=arr[mid]):
            return bin_sea(arr,l,mid-1,key)
        return bin_sea(arr,mid+1,h,key)
    
    if(key>=arr[mid] and k<=arr[h]):
        return bin_sea(arr,mid+1,h,key)
        
    return bin_sea(arr,l,mid-1,key)
        
    
while(t):
    le=int(raw_input())
    arr=[int(x) for x in raw_input().split()]
    key=int(raw_input())
    
    l=0
    h=le-1
    kata= bin_sea(arr,l,h,key)
    if(kata==-1):
        print "none"
    else:
        print kata
    t-=1
