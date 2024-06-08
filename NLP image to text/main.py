#install and run tesseract command https://youtu.be/Rb93uLXiTwA?si=E8j5nyhoq4tcCpzI

import cv2
import pytesseract
import numpy as np
import mahotas


def extract_text_from_image(image_path):
    try:
        img = cv2.imread(image_path)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        features = mahotas.features.zernike_moments(gray, 64, degree=8)  # 64 radius, 

        text = pytesseract.image_to_string(gray)

        return text
    except Exception as e:
        print("An error occurred:", e)
        return None

def main(): 
    image_path = '2.png' #enter image path here, make sure it is .png format or else convert online

    extracted_text = extract_text_from_image(image_path)

    if extracted_text is not None:
        print("Extracted Text:")
        print(extracted_text)
    else:
        print("Failed to extract text from the image.")

if __name__ == "__main__":
    main()
