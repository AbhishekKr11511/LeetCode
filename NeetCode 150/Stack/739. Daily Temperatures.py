'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
'''
def dailyTemperatures2(temps):
    output = []
    for i in range(len(temps)):
        j = i + 1
        while j < len(temps):
            if temps[j] > temps[i]:
                output.append(j-i)
                break
            j += 1
            if j == len(temps):
                output.append(0)
    output.append(0)
    return output


def dailyTemperatures2(temps):
    output = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and t>stack[-1][0]:
            stackT, stackInd = stack.pop()
            output[stackInd] = (i-stackInd)
        stack.append([t, i])
    return output


print(dailyTemperatures2([73,74,75,71,69,72,76,73]))