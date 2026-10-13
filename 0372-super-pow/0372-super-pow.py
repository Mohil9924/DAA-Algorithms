class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        a %= MOD
        
        result = 1
        for digit in b:
            # Raise current accumulated power to 10 and multiply by a^digit
            result = (pow(result, 10, MOD) * pow(a, digit, MOD)) % MOD
            
        return result