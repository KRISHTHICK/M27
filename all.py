def main(image_path, meme_text):
    # Step 1: Analyze the image
    image_label = analyze_image(image_path)
    
    # Step 2: Generate cartoon meme
    meme_path = generate_cartoon_meme(image_path, meme_text)
    
    # Step 3: Share on social media
    share_on_twitter(meme_path, f"Check out this meme! {image_label}")
    share_on_instagram(meme_path, f"Check out this meme! {image_label}")

# Example usage
main('path/to/your/image.jpg', 'This is a meme!')
