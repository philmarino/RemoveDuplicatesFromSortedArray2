def removeDuplicates(list):
    unique = []
    unique2 = []
    removables = []
    for index, item in enumerate(list):
        if item in unique:
            if item in unique2:
                removables.append(index)
            else:
                unique2.append(item)
        else:
            unique.append(item)
    #now we have a list of locations to be removed
    offset = 0
    for index in removables:
        list.pop(index-offset)
        offset += 1 #now that we removed an item, subsequent removables' index is off by one
    return len(list)


#Example 1:
#Input: 
nums = [1,1,1,2,2,3]
k = removeDuplicates(nums)
print(k)
print(nums)
#Output: 5, nums = [1,1,2,2,3,_]
#Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
#It does not matter what you leave beyond the returned k (hence they are underscores).

#Example 2:
#Input: 
nums = [0,0,1,1,1,1,2,3,3]
k = removeDuplicates(nums)
print(k)
print(nums)
#Output: 7, nums = [0,0,1,1,2,3,3,_,_]
#Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
#It does not matter what you leave beyond the returned k (hence they are underscores).
 