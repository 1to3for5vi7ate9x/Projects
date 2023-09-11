def solution(arr):
    ans = float('-inf')
    result = -1
    weight = [0] * len(arr)
    
    for i in range(len(arr)):
        source = i
        dest = arr[i]
        
        if dest != -1:
            weight[dest] += source
            
            if ans <= weight[dest]:
                ans = max(ans, weight[dest])
                result = dest
                
    if ans != float('-inf'):
        return result
    
    return -1


n = int(input(""))
input_list = list(map(int, input("").split()))

result = solution(input_list)
print(result)
