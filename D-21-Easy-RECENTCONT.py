def count_problems_in_contests():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])  # number of test cases
    results = []
    index = 1
    
    for _ in range(T):
        N = int(data[index])  # number of problems
        contest_codes = data[index + 1].split()  # list of contest codes
        count_start38 = contest_codes.count('START38')
        count_ltime108 = contest_codes.count('LTIME108')
        
        results.append(f"{count_start38} {count_ltime108}")
        index += 2  # move to the next test case
    
    # Print all results
    print("\n".join(results))

# Call the function to execute
count_problems_in_contests()