# получаем список чисел
# отсортировать in place без  использ встроенных функций
#  как вариант - пузырьком

nums = [0, -9, 8, 6, 99]

def my_sort(nums):
    for i, item in enumerate(nums):
        for j in range(i, len(nums)):
            if item > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    
my_sort(nums)
print(nums)#[-9, 0, 6, 8, 99]