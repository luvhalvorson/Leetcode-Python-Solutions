class MyCalendar:

    def __init__(self):
        self.bookeds = []
        

    def book(self, start: int, end: int) -> bool:
        # i = 0
        # while start < bookeds[i][0] and start < bookeds[i][1]:
        #     i += 1
        for i in range(len(self.bookeds)):
            if end <= self.bookeds[i][0]:
                # if end == self.bookeds[i][0]:
                #     self.bookeds[i] = [start, self.bookeds[i][1]] # 連起來了，第一項變成現在這個的頭，偽不變
                # else:
                self.bookeds.insert(i, [start, end])
                #print("sucess", [start, end], "||||||",self.bookeds)
                return True
            if start >= self.bookeds[i][0] and start < self.bookeds[i][1]:
                return False
            if end > self.bookeds[i][0] and end <= self.bookeds[i][1]:
                return False
            if start < self.bookeds[i][0] and end > self.bookeds[i][1]:
                return False
            if start > self.bookeds[i][0] and end < self.bookeds[i][1]:
                return False
        # if  self.bookeds and self.bookeds[-1][1] == start:
        #     self.bookeds[-1][1] = end
        # else:
        self.bookeds.append([start, end])
        
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)