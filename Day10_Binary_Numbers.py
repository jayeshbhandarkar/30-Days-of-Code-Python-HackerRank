import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    binary_representation = bin(n)[2:]
    
    consecutive_ones = binary_representation.split('0')
    
    max_consecutive_ones = max(len(seq) for seq in consecutive_ones)
    
    print(max_consecutive_ones)
