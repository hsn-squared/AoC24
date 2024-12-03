#day3pt1
import re

def extract_and_multiply(memory):
    # Regular expression to find valid mul(X,Y) instructions
    pattern = re.compile(r'mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)')
    
    # Find all matches in the memory
    matches = pattern.findall(memory)
    
    # Perform the multiplications and sum the results
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

# Read the corrupted memory from input3.txt
with open('3input.txt', 'r') as file:
    corrupted_memory = file.read()

# Calculate the sum of all valid multiplications
result = extract_and_multiply(corrupted_memory)
print(f"Sum of all valid multiplications: {result}")