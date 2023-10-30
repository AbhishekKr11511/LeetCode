def numberOfEmployeesWhoMetTarget(hours, target):
    count = 0
    for hour in hours:
        if(hour>=target):
            count = count +1
    
    return count

print(numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))
