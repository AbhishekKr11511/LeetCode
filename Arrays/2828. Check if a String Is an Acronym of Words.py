def isAcronym(words,s):
    acronym = ""
    for item in words:
        acronym=acronym+item[0]
    if acronym==s:
        return True
    else:
        return False
    
print(isAcronym(["alice","bob","charlie"], 'abc'))