class Solution(object):
    def maximumTime(self, time):
        time = list(time)
        
        # Hours: Tens place (time[0])
        if time[0] == '?':
            # If ones place is '0', '1', '2', '3', or '?', max tens digit is '2'
            # Otherwise (e.g. '4', '5', '6', ...), max tens digit is '1'
            if time[1] in ('?', '0', '1', '2', '3'):
                time[0] = '2'
            else:
                time[0] = '1'
                
        # Hours: Ones place (time[1])
        if time[1] == '?':
            # If tens place is '2', max ones digit is '3' (since max hour is 23)
            # Otherwise (tens place is '0' or '1'), max ones digit is '9'
            if time[0] == '2':
                time[1] = '3'
            else:
                time[1] = '9'
                
        # Minutes: Tens place (time[3])
        if time[3] == '?':
            time[3] = '5'
            
        # Minutes: Ones place (time[4])
        if time[4] == '?':
            time[4] = '9'
            
        return "".join(time)