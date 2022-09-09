class Solution:
    def isHappy(self, n: int) -> bool:
        all_results = set()
        while self.seen(n) not in all_results:
            all_results.add(self.seen(n))
            n = self.seen(n)
        return n == 1

    def seen(self, number):
        result = 0
        while number > 0:
            result += (number % 10) ** 2
            number //= 10
        return result

solution = Solution()
print(solution.isHappy(19))