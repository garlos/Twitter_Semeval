from tweepy_streamer import TwitterStreamer

# Authenticate using config.py and connect to Twitter Streaming API.
hash_tag_list = ["donal trump", "hillary clinton", "barack obama", "bernie sanders"]
fetched_tweets_filename = "tweets.txt"

twitter_streamer = TwitterStreamer()
twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)