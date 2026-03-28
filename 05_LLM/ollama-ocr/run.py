#!/usr/bin/env python
#date 2024-12-16
# run code about  7.8 min on cPU 

from ollama_ocr import OCRProcessor

# Initialize OCR processor
ocr = OCRProcessor(model_name='llama3.2-vision:11b')  # You can use any vision model available on Ollama

# Process an image
result = ocr.process_image(
    image_path="./image/invoice.png",
    format_type="markdown"  # Options: markdown, text, json, structured, key_value
)
with open('result.md', 'w') as f:
    f.write(result)


