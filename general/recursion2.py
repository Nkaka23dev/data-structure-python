def cal_sum(arr):
    if arr[0]:
        return arr[0]
    return arr[len(arr)-1]+cal_sum(arr[len(arr)-2])


if __name__=="__main__":
    elements=[23,10,12,18,25] 
    print(cal_sum(elements))
   
