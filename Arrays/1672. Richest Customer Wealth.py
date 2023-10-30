
def maximumWealth(accounts):
    for i in range(len(accounts)):
        total = sum(accounts[i])
        accounts[i] = total
    
    return max(accounts)

print(maximumWealth([[1,2,3],[3,2,1]]))