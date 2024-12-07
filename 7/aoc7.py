#!/usr/bin/env python3

testcase = False
if testcase:
    file = "test.txt"
else:
    file = "input.txt"

def TestWorks():
    return True

def Calculate(answer,nums):
    if(len(nums) == 1):
        return False
    test_ans1 = nums[0] * nums[1]
    test_ans2 = nums[0] + nums[1]
    if(len(nums) == 2 and (answer == test_ans1 or answer == test_ans2)):
        return True
    test1 = False
    if(test_ans1 <= answer):
        test_nums = [test_ans1] + nums[2:]
        test1 = Calculate(answer,test_nums)
    test2 = False
    if(test_ans2 <= answer):
        test_nums = [test_ans2] + nums[2:]
        test2 = Calculate(answer,test_nums)
    if(test1 or test2):
        return True
    else:
        return False
    
def Calculate2(answer,nums):
    if(len(nums) == 1):
        return False
    test_ans1 = nums[0] * nums[1]
    test_ans2 = nums[0] + nums[1]
    test_ans3 = int( str(nums[0]) + str(nums[1]))

    if(len(nums) == 2 and (answer == test_ans1 or answer == test_ans2 or answer == test_ans3) ):
        return True
    test1 = False
    if(test_ans1 <= answer):
        test_nums = [test_ans1] + nums[2:]
        test1 = Calculate2(answer,test_nums)
    test2 = False
    if(test_ans2 <= answer):
        test_nums = [test_ans2] + nums[2:]
        test2 = Calculate2(answer,test_nums)
    test3 = False
    if(test_ans3 <= answer):
        test_nums = [test_ans3] + nums[2:]
        test3 = Calculate2(answer,test_nums)

    if(test1 or test2 or test3):
        return True
    else:
        return False 

if(__name__ == '__main__'):

    try:
        stuff = open(file,"r")
    except FileNotFoundError:
        print("Gonna need an input file there, Bud.")
        exit(0)
    else:
        with stuff:
            lines = stuff.read().splitlines()

    total = 0
    total2 = 0
    for line in lines:
        (answer,numbers) = line.split(": ")
        answer = int(answer)
        nums = numbers.split(' ')
#        print(answer,nums)
        nums = [ int(x) for x in nums ]
        if Calculate(answer,nums):
            total += answer
        if Calculate2(answer,nums):
            total2 += answer

    print("Part1 :",total)
    print("Part2 :",total2)


