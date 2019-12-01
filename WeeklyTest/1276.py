"""
1276. Number of Burgers with No Waste of Ingredients

https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

Chickens and ducks in same cage question :)
x = 4a + b, y = 2a + b
Just remember to check x,y > 0 and the number is even
"""

class Solution:
    def numOfBurgers(self, a: int, b: int) -> List[int]:
        # x -> 4a + b, y -> 2a + b
        x = (a - b * 2) // 2
        y = b - x
        return [x,y] if x >= 0 and y >= 0 and (a - b * 2) % 2 == 0 else []
        
        
