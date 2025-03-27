from instabot import Bot

def share_on_instagram(meme_path, text):
    # Instagram credentials
    username = 'your_username'
    password = 'your_password'
    
    # Authenticate to Instagram
    bot = Bot()
    bot.login(username=username, password=password)
    
    # Upload the image
    bot.upload_photo(meme_path, caption=text)

# Example usage
share_on_instagram('cartoon_meme.jpg', 'Check out this meme!')
