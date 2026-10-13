class Solution(object):
    def minMovesToSeat(self, seats, students):
        # Sort both arrays in ascending order
        seats.sort()
        students.sort()
        
        total_moves = 0
        
        # Match each student to the corresponding seat
        for i in range(len(seats)):
            total_moves += abs(seats[i] - students[i])
            
        return total_moves