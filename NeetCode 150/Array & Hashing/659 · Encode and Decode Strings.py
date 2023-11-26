'''

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Example1
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example2
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;::;yes"
Tags

'''

def encode(strs):
    encodedString = ""
    for i in range(len(strs)):
        encodedString = encodedString + f"{len(strs[i])}" + "#" + strs[i]
    return encodedString



def decode(str):
    result = []
    i = 0
    while i < len(str):
        if str[i].isdigit() and str[i+1] == "#":
            tempString = ""
            for j in range(int(str[i])):
                tempString = tempString + str[i+2+j]
            result.append(tempString)
        i += int(str[i]) + 2
    return result


print(encode(["lint","code","love","you"]))
print(decode("4#lint4#code4#love3#you"))