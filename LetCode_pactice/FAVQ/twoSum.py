def towSum(nums, target):
    indexDic ={}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in indexDic:
            return [indexDic[complement], i]
    
        indexDic[num] = i

nums =[1,3,5,10,4]
target = 14
result = towSum(nums, target)
print(result)