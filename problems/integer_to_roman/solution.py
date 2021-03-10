class Solution:
    def intToRoman(self, num: int) -> str:
        string = str(num)
        mylist = [["M"], ["C", "D", "CD", "CM"], ["X", "L", "XL", "XC"], ["I", "V", "IV", "IX"]]
        answer = ""
        if len(string) > 3:
            answer += int(string[:-3]) * mylist[0][0]
        
        for i in range(-3, 0):
            if len(string) >= -i:
                if string[i]:
                    temp = int(string[i])
                    if temp == 9:
                        answer += mylist[i][3]
                    elif temp == 4:
                        answer += mylist[i][2]
                    elif temp  <= 3:
                        answer += mylist[i][0] * temp
                    else:
                        answer += (mylist[i][1] + mylist[i][0] * (temp - 5) )
        return answer