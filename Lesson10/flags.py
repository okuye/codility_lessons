"""
Task:Flags
Find the maximum number of flags that can be set on mountain peaks.

A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbours. More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly four peaks: elements 1, 3, 5 and 10.

You are going on a trip to a range of mountains whose relative heights are represented by array A, as shown in a figure below. You have to choose how many flags you should take with you. The goal is to set the maximum number of flags on the peaks, according to certain rules.



Flags can only be set on peaks. What's more, if you take K flags, then the distance between any two flags should be greater than or equal to K. The distance between indices P and Q is the absolute value |P − Q|.

For example, given the mountain range represented by array A, above, with N = 12, if you take:

two flags, you can set them on peaks 1 and 5;
three flags, you can set them on peaks 1, 5 and 10;
four flags, you can set only three flags, on peaks 1, 5 and 10.
You can therefore set a maximum of three flags in this case.

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the maximum number of flags that can be set on the peaks of the array.

For example, the following array A:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..400,000];
each element of array A is an integer within the range [0..1,000,000,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingKZZ92Z-HUN/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(A):
    # write your code in Python 3.6
    # 先找出peak的數目，再依序(1~len(A))計算兩兩之間的距離存入distances
    # 依序在distances中由大至小遍歷peak，當flag_count等於flag後回傳

    if len(A) < 3: return 0
    
    peaks = []
    distances = []

    for idx in range(1, len(A)-1):
        if A[idx-1] < A[idx] > A[idx+1]:
            peaks.append(idx)

    peak_num = len(peaks)
    if peak_num < 2: return peak_num
    
    for idx in range(1, peak_num):
        distances.append(peaks[idx] - peaks[idx-1])

    for flag in range(peak_num, 0, -1):
        tmp = 0
        check = distances.copy()
        flag_count = 1

        while check:
            tmp += check[0]
            check = check[1:]
            if tmp >= flag:
                tmp = 0
                flag_count += 1

        if flag_count == flag:
            return flag_count

    return 0

#testcase 1
A = [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
print(solution(A))


#testcase 2
A = [1, 3, 2]
print(solution(A))

# testcase 3
A = [0, 0, 0, 0, 0, 1, 0, 1, 0, 1]
print(solution(A))