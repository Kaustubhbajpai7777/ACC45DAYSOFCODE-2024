# cook your dish here
import math

def min_attacks(test_cases):
    results = []
    
    for H, X, Y in test_cases:
        health_after_special = H - Y
        if health_after_special <= 0:
            attacks_with_special = 1
        else:
            normal_attacks_needed = math.ceil(health_after_special / X)
            attacks_with_special = 1 + normal_attacks_needed
            
        normal_attacks_only = math.ceil(H / X)
        
        min_attacks_needed = min(attacks_with_special, normal_attacks_only)
        
        results.append(min_attacks_needed)
    
    return results

T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

results = min_attacks(test_cases)

for result in results:
    print(result)
