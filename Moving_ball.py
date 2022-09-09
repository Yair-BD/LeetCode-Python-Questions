#1769. Minimum Number of Operations to Move All Balls to Each Box
# O(n^2)
from black import main
import numpy as np
class Solution:
    def minOperations(boxes: str):
       # אני יכול לעבור על כל הסטרינג ושלמור לי במערך באיזה מיקומים יש לי אחד 
       # אחרי זה אני עובר שוב כל מיקום ואז מחשב כמה יקח לי למיקום הזה להעביר מכל המיקומים אליו נגיד אני נמצא עכשיו במיקום אחד אז בשביל להעביר ממיקום שלוש אליו אני צריך לעשות שלוש פחות אפס ועוד שמונה פחות 0
       # זה פוטר לי את העניין מאותו מקום כי נגיע מיקום 3 פםפםחות שלוש מאפס לי 
       
        index_of_1 = []
        for i in range(len(boxes)):
            if boxes[i] == "1":
               index_of_1.append(i)
        
        sum_of_operation = 0
        answer = []
        for i in range(len(boxes)):
            for j in index_of_1:
                sum_of_operation += abs(i - j)
            answer.append(sum_of_operation)
            sum_of_operation = 0    
        return answer
    
    
    def minOperations_numpy(boxes: str): 
        index_of_1 = []
        for i in range(len(boxes)):
            if boxes[i] == "1":
                index_of_1.append(i)
        index_of_1 = np.array(index_of_1)

        
        answer = []
        for i in range(len(boxes)):
            answer.append(sum(abs(index_of_1 - i )))  
        
        return answer
    
    
    def minOperations_lean(boxes: str): 
    #"1110"
    #
        lCount, lCost, rCount, rCost, n = 0, 0, 0, 0, len(boxes)
        ans = [0] * n
        for i in range(1, n):
            if boxes[i-1] == '1': # אני תמיד בודק את מי שלפני כדי לדעת האם להוסיף למעבר אליי עוד פעולה מעבר לפעולת הקיבוץ לאינדקס לפני
                lCount += 1
            lCost += lCount
            ans[i] = lCost
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1':
                rCount += 1
            rCost += rCount
            ans[i] += rCost
        return ans
    
    print(minOperations_lean("110"))