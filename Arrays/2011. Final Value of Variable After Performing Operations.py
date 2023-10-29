def finalValueAfterOperations(operate):
    x = 0
    for i in range(len(operate)):
        if(operate[i]=="++X" or "X++"):
            x = x + 1;
        elif(operate[i]=="--X" or "X--"):
            x = x - 1;
    
    return x


print(finalValueAfterOperations(["++X","++X","X++"]))