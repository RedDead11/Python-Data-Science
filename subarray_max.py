nums = [5, 4, -1, 7, 8]

max_sum = 0

for i in range(len(nums)-1):
    if nums[i] > nums[i+1] and nums[i] > max_sum:
        max_sum = nums[i] + nums[i+1]
        print("Max Sum (if i>i+1):" + str(max_sum))
       
        # if max_sum < max_sum + nums[i+2]:
        #     max_sum = max_sum + nums[i+2]
        #     print(max_sum)
        #     print()
    else:
        print(max_sum)
        print()

print("a")
print(max_sum)
