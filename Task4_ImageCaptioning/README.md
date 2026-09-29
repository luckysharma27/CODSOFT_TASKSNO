# CODSOFT AI Internship - Task 4

## Image Captioning

### Objective
Build an AI-based image captioning system that analyzes an image and generates a meaningful text description.

### Description
This project uses a pretrained BLIP image-to-text model to generate captions for images. The user provides an image path, and the program returns an automatically generated caption.

### Technologies Used
- Python
- Hugging Face Transformers
- PyTorch
- PIL (Pillow)
- BLIP Image Captioning Model

### Features
- Accepts an image path from the user
- Loads the selected image
- Uses a pretrained AI model to understand the image
- Generates a natural-language caption
- Handles invalid image paths
- Provides an exit option

### How It Works
1. The program loads the BLIP image-to-text model.
2. The user enters the path of an image.
3. Pillow opens the image.
4. The image is passed to the pretrained BLIP model.
5. The model generates a caption.
6. The generated caption is displayed in the terminal.

### Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

If you have multiple Python versions:

```bash
py -3.13 -m pip install -r requirements.txt
```

### How to Run

```bash
python image_captioning.py
```

Or:

```bash
py -3.13 image_captioning.py
```

On the first run, the pretrained model is downloaded automatically from Hugging Face. An internet connection is required for the initial model download.

### Example

```text
======================================
        IMAGE CAPTIONING SYSTEM
======================================

Enter image path or type 'exit':

Image path: dog.jpg

Generated Caption:
a dog sitting on the grass
```

### Learning Outcomes
- Understanding image captioning
- Using pretrained AI models
- Image preprocessing
- Natural language generation
- Working with computer vision and NLP together
- Using Hugging Face Transformers

### Author
Lucky Sharma

### Internship
CodSoft Artificial Intelligence Internship
