
import tweepy

def share_on_twitter(meme_path, text):
    # Twitter API credentials
    consumer_key = 'your_consumer_key'
    consumer_secret = 'your_consumer_secret'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'
    
    # Authenticate to Twitter
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    
    # Upload and tweet the image
    api.update_with_media(meme_path, text)

# Example usage
share_on_twitter('cartoon_meme.jpg', 'Check out this meme!')
