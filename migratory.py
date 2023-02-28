import sys
from collections import Counter

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
freq = Counter(types)
print(max(freq, key=freq.get))
