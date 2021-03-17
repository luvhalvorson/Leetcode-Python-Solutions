class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        r = self.radius
        xc = self.x_center
        yc = self.y_center
        theta = 2 * 3.14 * random.random()
        leng = math.sqrt(random.random()) * r;
        return [xc + leng * math.cos(theta), yc + leng * math.sin(theta)]
# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()