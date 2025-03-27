from PIL import Image, ImageDraw, ImageFont

def generate_cartoon_meme(image_path, text):
    # Open the image
    image = Image.open(image_path)
    
    # Apply a cartoon effect (simple edge detection for illustration)
    image = image.convert('L')  # Convert to grayscale
    edges = image.filter(ImageFilter.FIND_EDGES)
    
    # Draw the text on the image
    draw = ImageDraw.Draw(edges)
    font = ImageFont.truetype("arial.ttf", 40)
    text_position = (10, 10)
    draw.text(text_position, text, font=font, fill="white")
    
    # Save the cartoon meme
    meme_path = 'cartoon_meme.jpg'
    edges.save(meme_path)
    
    return meme_path

# Example usage
meme_path = generate_cartoon_meme('path/to/your/image.jpg', 'This is a meme!')
print(f"Cartoon meme saved at: {meme_path}")
