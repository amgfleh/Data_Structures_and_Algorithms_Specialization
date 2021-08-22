# python3
import random

def max_pairwise_product(numbers):
    n = len(numbers)
    if n==1:
        return numbers[0]
    elif numbers == []:
        return 0
    max_num_1 = 0
    for first in range(n):
            max_num_1 = max(numbers[first], max_num_1)
    index_1 = numbers.index(max_num_1)

    max_num_2 = 0
    for first in range(n):
        if first is not index_1:
            max_num_2 = max(numbers[first], max_num_2)

    return(max_num_1 * max_num_2)

def max_pairwise_cheating(b):
    if len(b)>=2:
        num_1 = max(b)
        b.remove(num_1)
        num_2 = max(b)
        correct_ans = num_1 * num_2
    else:
        correct_ans = b[0]
    return correct_ans

if __name__ == '__main__':
    while False:
        n = random.randint(1, 11)
        randomlist = []
        for i in range(n):
            num = random.randint(0, 99)
            randomlist.append(num)
        ans = max_pairwise_product(randomlist)
        b = randomlist.copy()
        if len(b)>=2:
            num_1 = max(b)
            b.remove(num_1)
            num_2 = max(b)
            correct_ans = num_1 * num_2
        else:
            correct_ans = b[0]
        if ans == correct_ans:
            print(ans, correct_ans)
            print("OK")
        else:
            print(n)
            print(randomlist)
            print(ans, correct_ans)
            print("Not")
            break
    
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_cheating(input_numbers))



