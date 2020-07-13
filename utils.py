from datetime import datetime, timedelta

def calculateElapsedTime(dt):
    """Calculate elapsed time from now.

    Returns a tuple containing the aproximated elapsed time and unit of time.
    """
    
    now = datetime.now()
    delta = now - dt

    str_elapsed = str(delta)

    if ',' in str_elapsed:
        t, u = str_elapsed[0 : str_elapsed.index(",")].split(' ')
        return (int(t), u)
    else:
        h, m, s = str_elapsed.split(':')

        H = int(h)
        if H > 0:
            return (H, "hours")

        M = int(m)
        if M > 0:
            return (M, "minutes")

        S = float(s)
        return (S, "seconds")
        
