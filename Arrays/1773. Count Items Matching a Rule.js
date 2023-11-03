link = 'https://leetcode.com/problems/count-items-matching-a-rule/'


// Solution
//---------------------------------
const countMatches = (items, ruleKey, ruleValue) => {
    let count = 0
    for (let i = 0; i < items.length; i++) {
        switch (ruleKey) {
            case 'type':
                if(items[i][0]===ruleValue) count++
                break;
                
            case 'color':
                if(items[i][1]===ruleValue) count++
                break;
            case 'name':
                if(items[i][2]===ruleValue) count++
                break;
        
            default:
                break;
        }
    }
    return count
}
//---------------------------------
let result = countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver")

console.log(result)