# 0 1 1 2 3 5 8 13

def fibonnaci(length):
    num1 = 0
    num2 = 1
    all_nums = [num1]

    for i in range(0, length):
        num1, num2 = num2, num1 + num2
        all_nums.append(num2)
    for i in range(len(all_nums)):
        if i % 2 == 0:
            print(all_nums[i], end=' ')



fibonnaci(10)
