class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        # Helper function to compute minimum finish time for Order: Category 1 -> Category 2
        def calc(start1, dur1, start2, dur2):
            # 1. Earliest finish time of any ride in Category 1
            min_finish_1 = min(s + d for s, d in zip(start1, dur1))
            
            # 2. Earliest finish time of Category 2 starting after min_finish_1
            return min(max(s, min_finish_1) + d for s, d in zip(start2, dur2))

        # Order A: Land ride first, then Water ride
        land_first = calc(landStartTime, landDuration, waterStartTime, waterDuration)
        
        # Order B: Water ride first, then Land ride
        water_first = calc(waterStartTime, waterDuration, landStartTime, landDuration)
        
        return min(land_first, water_first)