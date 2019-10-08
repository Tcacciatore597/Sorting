# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    #compare each element in arrA to each element in arrB.
 
    #take the lower element and append it to merged_arr
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    #check if length of array is < 2 elements.  if so return.
    n = len(arr)
    #find a middle position
    if n < 2:
        return
    #split list
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]
        merge(a, b)
    #merge()
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
