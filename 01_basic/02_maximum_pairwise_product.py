"""
Find the maximum of pairwise products from a list of integers.
"""

import random
from time import process_time_ns
from argparse import ArgumentParser

def maximum_pairwise_product(numbers):
    l = len(numbers)

    pdt = 0
    for i in range(l):
        for j in range(i+1, l):
            pdt = max(pdt, numbers[i] * numbers[j])
    
    print(pdt)

def maximum_pairwise_product_fast(numbers):
    max1 = max(numbers)
    numbers.pop(numbers.index(max1))
    
    print(max1 * max(numbers))

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--n_tests', type=int, required=False, default=0, help='Number of test cases to run.')
    parser.add_argument('--seed', type=int, required=False, default=0, help='Random state seed.')
    
    return parser.parse_args()

if __name__ == '__main__':
    start = process_time_ns()
    
    args = parse_args()
    if args.n_tests:
        random.seed(args.seed)
        for t in range(args.n_tests):
            l = random.randint(2, 1000)
            numbers = [random.randint(0, 100000) for _ in range(l)]
            print(l)
            print(numbers)
            r1 = maximum_pairwise_product(numbers)
            r2 = maximum_pairwise_product_fast(numbers)
            assert r1 == r2, f'Mismatch: r1 = {r1} | r2 = {r2}'
            print(r2)
            print()
    else:
        _ = int(input())
        numbers = list(map(int, input().split()))
        maximum_pairwise_product_fast(numbers)
    
    print(process_time_ns() - start)
