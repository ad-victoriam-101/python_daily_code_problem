class Solution:
    def hamming_distance(self, x: int, y: int) -> int:
        """
        Args:
            x:int
            y:int

        Returns:
            value associated to the Difference between two binary points.
        """
        answer = 0
        for i in range(31, -1, -1):
            binary1 = x >> i & 1
            binary2 = y >> i & 1
            answer += not (binary1 - binary2)
        return answer

    def hamming_distance_short(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')
