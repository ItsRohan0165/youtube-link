import decimal

def getElapsedTime(time):

    day = time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time

    return int(day), int(hour), int(minutes), int(seconds)