import cv2
import numpy as np
import tensorflow as tf

def analyze_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Preprocess the image (resize, normalize, etc.)
    resized_image = cv2.resize(image, (224, 224))
    normalized_image = resized_image / 255.0
    
    # Load a pre-trained model (e.g., MobileNetV2)
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    
    # Perform image analysis
    predictions = model.predict(np.expand_dims(normalized_image, axis=0))
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)
    
    return decoded_predictions[0][0][1]  # Return the label of the top prediction

# Example usage
image_label = analyze_image('path/to/your/image.jpg')
print(f"Image label: {image_label}")
