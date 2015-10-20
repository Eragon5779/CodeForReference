def longest_possible(playback):
    longest = 0
    name = ""
    for x in songs:
        time = map(int, x["playback"].split(':'))
        time = time[0] * 60 + time[1]
        if time > longest and time <= playback:
            longest = time
            name = x['title']
    return (False, name)[name != ""]
