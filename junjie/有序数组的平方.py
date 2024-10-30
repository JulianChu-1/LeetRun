#双指针法

def sortedSquare(x):
    j ,k, l= 0, len(x) - 1, len(x) - 1
    results = [float('inf')] * len(x)
    while j <= k:
        if(x[j] ** 2 > x[k] ** 2):
            results[l] = x[j] ** 2
            j += 1
        else:
            results[l] = x[k] ** 2
            k -= 1
        l -= 1
    return results

