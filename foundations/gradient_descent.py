class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        result = init
        for i in range(iterations):
            d = 2*result
            result = result -  learning_rate * d 

        return round(result,5)
    