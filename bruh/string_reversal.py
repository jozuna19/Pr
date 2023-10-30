""""
One of the basic ways to test the Python developer's problem-solving 
skills is by asking them how they would reverse a string, 
knowing how to do this is very useful in the production environment.
"""

#slice func
# str[start:stop:step] | extended slice syntax

trial = "reversal"
new_trial = trial[::-1] # [::-1] allows string to be outputed in reverse
print(new_trial)


#recurssion
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
    
str = "reversal"
reverse = string_reverse(str)

print(reverse)