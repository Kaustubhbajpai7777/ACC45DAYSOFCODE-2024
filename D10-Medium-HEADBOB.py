# cook your dish here
def identify_nationality(gestures):
    results = []
    for gesture in gestures:
        if 'I' in gesture:
            results.append("INDIAN")
        elif 'Y' in gesture:
            results.append("NOT INDIAN")
        else:
            results.append("NOT SURE")
    return results

T = int(input())
gestures = []

for _ in range(T):
    N = int(input())  
    gesture_string = input().strip()  
    gestures.append(gesture_string)

results = identify_nationality(gestures)

for result in results:
    print(result)