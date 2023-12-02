'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''

def checkInclusion(s1, s2):
        myList = list(s1)
        i = 0
        j = len(s1)-1
        result = False
        while j < len(s2):
            for k in range(len(s1)):
                if s2[i+k] in myList:
                    result = True
                    myList.remove(s2[i+k])
                else:
                    myList = list(s1)
                    result = False
                    break
            if len(myList) == 0 and result == True:
                return True
            i += 1
            j += 1

        return result

#---------------------------------------------------------
def isAnagram(s, t):
    if len(s)!=len(t):
        return False
    ss = list(s)
    tt = list(t)
    ss.sort()
    tt.sort()
    return ss == tt

def checkInclusion2(s1, s2):
    i = 0
    j = len(s1)-1
    result = False
    while j < len(s2):
        result = result or isAnagram(s1, s2[i:j+1])
        if result:
            return True
        i += 1
        j += 1
    return result
# -----------------------------------------------------
def checkInclusion3(s1, s2):
    if len(s1) > len(s2):
        return False
    s1Count, s2Count = [0] *26 ,[0]* 26
    for i in range(len(s1)):
        s1Count[ord(s1[i])- ord('a')] += 1
        s2Count[ord(s2[i])- ord('a')] += 1

    matches = 0
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)
    
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26: return True
        
        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1
        
        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
    
    return matches == 26

print(checkInclusion2("ab", "eidbaooo"))