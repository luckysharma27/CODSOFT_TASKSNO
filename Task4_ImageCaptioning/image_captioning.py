from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os

MODEL_NAME = "Salesforce/blip-image-captioning-base"

print("======================================")
print("        IMAGE CAPTIONING SYSTEM")
print("======================================")
print("\nLoading AI model...")
print("The first run may take some time because the model is downloaded.")

processor = BlipProcessor.from_pretrained(MODEL_NAME)
model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME)

print("\nModel loaded successfully!")

while True:
    image_path = input("\nEnter image path or type 'exit': ")

    if image_path.lower() == "exit":
        print("\nThank you for using the Image Captioning System!")
        break

    image_path = image_path.strip().strip('"')

    if not os.path.isfile(image_path):
        print("Image not found. Please enter a valid image path.")
        continue

    try:
        image = Image.open(image_path).convert("RGB")
        inputs = processor(images=image, return_tensors="pt")
        output = model.generate(**inputs, max_new_tokens=30)
        caption = processor.decode(output[0], skip_special_tokens=True)

        print("\nGenerated Caption:")
        print(caption)

    except Exception as e:
        print("\nUnable to process the image.")
        print("Error:", e)
