from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            x = (num - 3) // 3
            return [x, x + 1, x + 2]
        else:
            return []


if __name__ == "__main__":
    sol = Solution()
    print(sol.sumOfThree(33))   # Expected: [10, 11, 12]
    print(sol.sumOfThree(4))    # Expected: []
