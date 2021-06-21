"""

Case-specific Sorting of Strings 
Medium Accuracy: 61.53% Submissions: 9265 Points: 4
Given a string S consisting of uppercase and lowercase characters. The task is to sort uppercase and lowercase letters separately such that if the ith place in the original string had an Uppercase character then it should not have a lowercase character after being sorted and vice versa.

Example 1:

Input:
N = 12
S = defRTSersUXI
Output: deeIRSfrsTUX
Explanation: Sorted form of given string
with the same case of character as that
in original string is deeIRSfrsTUX
Example 2:

Input:
N = 6
S = srbDKi
Output: birDKs
Explanation: Sorted form of given string
with the same case of character will
result in output as birDKs.
Your Task:
You only need to complete the function caseSort that returns sorted string.

Expected Time Complexity: O(N*Log(N)).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 103

"""
def caseSort(s,n):
    #code here
    s1=[]
    res=[]
    res1=[]
    result=[]
    for i in s:
        if i.isupper():
            res.append(i)
            s1.append(0)
        elif i.islower():
            res1.append(i)
            s1.append(1)
    res ="".join(res)
    res1="".join(res1)
    res = sorted(res)
    res1 = sorted(res1)
    k=0
    j=0
    #print("res",res)
    #print("res1",res1)
    for i in s1:
        if i==1:
            result.append(res1[k])
            k+=1
        else:
            result.append(res[j])
            j+=1
    return("".join(result))
s = input()
print(caseSort(s,len(s)))
