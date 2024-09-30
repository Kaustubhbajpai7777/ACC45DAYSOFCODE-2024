# cook your dish here
def is_easy_to_pronounce(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consecutive_consonants = 0
    
    for char in s:
        if char in vowels:
            consecutive_consonants = 0  # Reset count on vowel
        else:
            consecutive_consonants += 1  # Increment on consonant
            
            if consecutive_consonants >= 4:
                return "NO"  # Hard to pronounce
            
    return "YES"  # Easy to pronounce

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    T = int(data[0])  # Number of test cases
    results = []
    
    index = 1
    for _ in range(T):
        N = int(data[index])  # Length of string S (not really needed)
        S = data[index + 1]  # The string S
        results.append(is_easy_to_pronounce(S))
        index += 2
        
    # Output results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
