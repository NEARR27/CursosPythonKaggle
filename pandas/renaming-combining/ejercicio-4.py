left = powerlifting_meets.set_index('MeetID')
right = powerlifting_competitors.set_index('MeetID')
powerlifting_combined = left.join(right)

# Check your answer
q4.check()
powerlifting_combined
