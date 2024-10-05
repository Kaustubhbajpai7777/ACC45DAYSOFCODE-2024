# cook your dish here
def is_pseudo_sorted(arr):
    n = len(arr)
    violation_index = -1
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            if violation_index != -1:  # More than one violation
                return "NO"
            violation_index = i
    
    if violation_index == -1:
        return "YES"  # Already sorted
    
    i = violation_index
    
    can_swap = True
    if i > 0:
        if arr[i - 1] > arr[i + 1]:  # arr[i+1] would take arr[i]'s position
            can_swap = False
            
    if i + 2 < n:
        if arr[i] > arr[i + 2]:  # arr[i] would take arr[i+1]'s position
            can_swap = False
            
    return "YES" if can_swap else "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = is_pseudo_sorted(arr)
    print(result)
