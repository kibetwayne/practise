def print_list(*arg):
    print(f'the list contains: {arg}')
    
print_list('eggs', 'bread', 'peanut butter')

def new(*args):
    print(f'{args} are thw new kids')
new('mathew', 'john')

#!================================================================

#number of days per month, 1st value is a place holder
month_days = [1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    return 29 if month == 2 and is_leap_year(year) else month_days[month]

print(days_in_month(2020, 3))

#!================================================================
'''write a function to find the missing positive number in a given list of numbers'''
def find_missing_number(numbers):
    n = len(numbers) + 1 
    expected_sum = n * (n + 1) // 2 
    actual_sum = sum(numbers)      
    return expected_sum - actual_sum

missing_number = find_missing_number([1,2,3,5])
print(missing_number)

#!================================================================
'''function that turns DNA to mRNA'''
def transcribe_to_mrna(dna):
    switch = {
        'A': 'U',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    mrna = []
    for l in dna:
        if l  not in switch:
            continue
        mrna.append(switch[l])
    return ''.join(mrna)

transcribe_to_mrna('ACGT')   

transcribe_to_mrna('ACGT')
def transcribe_to_mrna(dna):
    switch = {
        'A': 'U',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return ''.join(switch[base] for base in dna )
    

transcribe_to_mrna('ACGT')

#!================================================================
''' A function to sollve the exponential equation using'''
def solve_exponential(base, result):
    num = 0
    while  result > 1:
        if result % base != 0:
            return -1  
        result //= base   # result = result / base
        num += 1
        
    return num

print(solve_exponential(2, 8))

def solve_exponential(base, result):
    answer = 1
    while True:
        if (base**answer == result):
            return answer
        answer += 1
        
print(solve_exponential(2, 8))

import math
def solve_exponential(base, result):
    return round(math.log(result,base))

#!================================================================
'''join two sets'''
def get_union(set1, set2):
    new = set1.union(set2)
    print(new)
    
    
get_union({1, 2, 3}, {2, 3, 4})

#!================================================================
'''reverse a string'''
name = 'tap water' #A step of -1 moves backward through 
print(name[::-1])

#!================================================================
#?looping over nested lists
'''print vertically'''
strings = ["abcqwe", "def", "ghiq"]
length = max(len(word) for word in strings)

for i in range(length):
    line = ""
    for word in strings:
        line += word[i] if i < len(word) else " "
    print(line)