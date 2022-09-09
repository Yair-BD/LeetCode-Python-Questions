def longestCommonPrefix(strs: list[str]) -> str:
    i = 0
    common = ""
    while i < len(min(strs, key = len)):
        letter = strs[0][i]
        for str in strs:
            if letter != str[i]:
                return common

        i += 1

        common += letter
    return common

            
                
    """שלבי עבודה
    אני רוצה לעבור על כל האותיות - סדר גודל של האותיות זה לפי המילה הכי קטנה
    אני עובר מילה מילה באות משותפת לכולם
    אם האות משותפת לכולם - ממשיך עד הסוף 
    אם שונה - מחזיר את המשותף שהיה לי עד עכשיו  
    """
    
print(longestCommonPrefix(["ower", "flow", "ihgt", "rgre"]))# 6, 6, 6 = 16 אורך הכי קצר * אורך המערך= 16