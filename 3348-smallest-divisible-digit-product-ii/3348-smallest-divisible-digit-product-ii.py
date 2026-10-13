class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Prime factorize t into powers of 2, 3, 5, 7
        req = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in (2, 3, 5, 7):
            while t % p == 0:
                req[p] += 1
                t //= p
        if t > 1:
            return "-1"  # Impossible if t has prime factors > 7

        def get_f(d):
            return {
                1: (0, 0, 0, 0), 2: (1, 0, 0, 0), 3: (0, 1, 0, 0), 4: (2, 0, 0, 0), 5: (0, 0, 1, 0),
                6: (1, 1, 0, 0), 7: (0, 0, 0, 1), 8: (3, 0, 0, 0), 9: (0, 2, 0, 0)
            }[d]

        # Dynamic programming cache for min digits needed for remaining (c2, c3, c5, c7)
        def min_needed_len(c2, c3, c5, c7):
            c2, c3, c5, c7 = max(0, c2), max(0, c3), max(0, c5), max(0, c7)
            min_23 = float('inf')
            for k in range(min(c2, c3) + 1):
                rem2, rem3 = max(0, c2 - k), max(0, c3 - k)
                digits = k + (rem2 + 2) // 3 + (rem3 + 1) // 2
                min_23 = min(min_23, digits)
            return min_23 + c5 + c7

        def can_fill(rem, c2, c3, c5, c7):
            return min_needed_len(c2, c3, c5, c7) <= rem

        def fill_min(rem, r2, r3, r5, r7):
            res = []
            for pos in range(rem):
                for d in range(1, 10):
                    f2, f3, f5, f7 = get_f(d)
                    if can_fill(rem - 1 - pos, r2 - f2, r3 - f3, r5 - f5, r7 - f7):
                        res.append(str(d))
                        r2, r3, r5, r7 = r2 - f2, r3 - f3, r5 - f5, r7 - f7
                        break
            return "".join(res)

        # 1. Check if num itself works (only if zero-free)
        if '0' not in num:
            r2, r3, r5, r7 = req[2], req[3], req[5], req[7]
            for ch in num:
                f2, f3, f5, f7 = get_f(int(ch))
                r2, r3, r5, r7 = r2 - f2, r3 - f3, r5 - f5, r7 - f7
            if r2 <= 0 and r3 <= 0 and r5 <= 0 and r7 <= 0:
                return num

        n = len(num)
        first_zero = num.find('0')
        max_p = n if first_zero == -1 else first_zero

        # Precompute prefix requirements up to max_p
        pref = list(req.values())
        for i in range(max_p):
            f = get_f(int(num[i]))
            pref = [pref[k] - f[k] for k in range(4)]

        # 2. Case A: Change digit at first '0' position to something >= 1
        if first_zero != -1:
            i = first_zero
            for d in range(1, 10):
                f = get_f(d)
                if can_fill(n - 1 - i, pref[0] - f[0], pref[1] - f[1], pref[2] - f[2], pref[3] - f[3]):
                    return num[:i] + str(d) + fill_min(n - 1 - i, pref[0] - f[0], pref[1] - f[1], pref[2] - f[2], pref[3] - f[3])

        # 3. Case B: Try incrementing digit BEFORE the first zero (right-to-left)
        for i in range(max_p - 1, -1, -1):
            f_orig = get_f(int(num[i]))
            pref = [pref[k] + f_orig[k] for k in range(4)]
            
            for d in range(int(num[i]) + 1, 10):
                f = get_f(d)
                if can_fill(n - 1 - i, pref[0] - f[0], pref[1] - f[1], pref[2] - f[2], pref[3] - f[3]):
                    return num[:i] + str(d) + fill_min(n - 1 - i, pref[0] - f[0], pref[1] - f[1], pref[2] - f[2], pref[3] - f[3])

        # 4. If length N is impossible, expand to target length
        target_len = max(n + 1, min_needed_len(req[2], req[3], req[5], req[7]))
        return fill_min(target_len, *req.values())