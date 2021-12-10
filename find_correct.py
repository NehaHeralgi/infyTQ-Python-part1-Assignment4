'''
Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. 
Assume that the words contain only uppercase letters and the maximum word length is 10.
'''

#lex_auth_01269444890062848087

def find_correct(word_dict):
    #start writing your code here
    correct=0 
    almost=0 
    wrong=0 
    for key,value in word_dict.items():
        count=0 
        if(key==value):
            correct+=1 
        elif(len(key)==len(value)):
            for i in range(0,len(value)):
                if(key[i]!=value[i]):
                    count+=1 
            if count<=2:
                almost+=1 
            else:
                wrong+=1 
        else:
            wrong+=1 
    list=[correct,almost,wrong]
    return list

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))