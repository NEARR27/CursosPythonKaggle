# Your code here
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()

# Check your answer
q1.check()
reviews_written
