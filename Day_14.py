# -------- DAY 14 "Tweet" --------
# Goal: Write as twitter that takes 280 characters in one tweet.
while True:
    tweet = input('Write new tweet..\n')
    # It should greater than 280 but this is as an experiment
    if len(tweet) > 28:
        print('Your tweet exceeds the character limit (280)!\n', '~'*20)
        continue
    break
