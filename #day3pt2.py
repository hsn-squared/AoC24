#day3pt2

import re

def extract_and_multiply(memory):
    # Regular expression to find valid mul(X,Y), do(), and don't() instructions
    pattern = re.compile(r'(mul\(\s*\d{1,3}\s*,\s*\d{1,3}\s*\))|(do\(\))|(don\'t\(\))')
    
    # Find all matches in the memory
    matches = pattern.findall(memory)
    
    # Initialize variables
    total_sum = 0
    mul_enabled = True
    
    # Process each match
    for match in matches:
        mul_match, do_match, dont_match = match
        if mul_match:
            numbers = re.findall(r'\d+', mul_match)
            if len(numbers) == 2:
                x, y = numbers
                if mul_enabled:
                    total_sum += int(x) * int(y)
                    print(f"Enabled mul({x},{y}) = {int(x) * int(y)}")
        elif do_match:
            mul_enabled = True
            print("do() encountered, enabling mul instructions")
        elif dont_match:
            mul_enabled = False
            print("don't() encountered, disabling mul instructions")
    
    return total_sum

# Read the corrupted memory from 3input.txt
with open('3input.txt', 'r') as file:
    corrupted_memory = file.read()

# Calculate the sum of all valid multiplications
result = extract_and_multiply(corrupted_memory)
print(f"Sum of all valid multiplications: {result}")
