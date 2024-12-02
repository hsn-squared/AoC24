def isitreallysafe(levels):
    diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    return all(1 <= abs(d) <= 3 for d in diffs) and (all(d > 0 for d in diffs) or all(d < 0 for d in diffs))
 
safe = 0
with open('input.txt', 'r') as f:
    for line in f:
        levels = list(map(int, line.split()))
        if isitreallysafe(levels):
            safe += 1 
        else:
            for i in range(len(levels)):
                modifiedlevels = levels[:i] + levels[i + 1:]  
                if isitreallysafe(modifiedlevels):
                    safe += 1
                    break
print(safe)