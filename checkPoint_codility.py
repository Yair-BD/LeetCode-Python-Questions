# get k number of char and masssage 
# i return the message with the k number of char
def solution(message, K):
    # write your code in Python 3.6
    message_after_k = message[:K] # get the first K char of message
    splited_message_after_k = message_after_k.split() # split the message with space we know there is only one space
    splited_message = message.split() # split the message with space
   
    index_of_last_word = len(splited_message_after_k) - 1 # get the index of the last word that can be the problem
    
    if splited_message[index_of_last_word] == splited_message_after_k[index_of_last_word]:  # we cut perfectly the message
        
        return " ".join(splited_message_after_k)
    
    else:
        splited_message_after_k.pop() # remove the last word of the message becouse its not valid
        return " ".join(splited_message_after_k)
s = solution("To crop or not to crop", 17)
print(s)
print(len(s))