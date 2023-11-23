# In Python we can compare 2 arrays like : arr1 == arr2

def isAnagram(s, t):
    if len(s)!=len(t):
        return False
    ss = list(s)
    tt = list(t)
    ss.sort()
    tt.sort()
    return ss == tt

print(isAnagram("car", "rat"))