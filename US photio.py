import cv2
import numpy as np
import os

def load_image(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return None
    image = cv2.imread(file_path)
    if image is None:
        print(f"Error: Unable to read the image file '{file_path}'.")
        return None
    return image

def generate_passport_photo(image):
    # Convert to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) == 0:
        print("No face detected in the image. Please try a different photo.")
        return None
    
    # Use the first detected face
    (x, y, w, h) = faces[0]
    
    # Calculate dimensions
    head_height = int(h * 1.4)  # Head height should be about 1 inch (25.4 mm)
    total_height = int(head_height / 0.7)  # Total height should be about 2 inches (51 mm)
    total_width = int(total_height * 2 / 2)  # Aspect ratio should be 2:2.5
    
    # Calculate crop area
    center_x = x + w // 2
    center_y = y + h // 2
    crop_top = max(center_y - total_height // 2, 0)
    crop_bottom = min(center_y + total_height // 2, image.shape[0])
    crop_left = max(center_x - total_width // 2, 0)
    crop_right = min(center_x + total_width // 2, image.shape[1])
    
    # Crop and resize
    passport_photo = image[crop_top:crop_bottom, crop_left:crop_right]
    passport_photo = cv2.resize(passport_photo, (600, 600))  # 2x2.5 inches at 300 dpi
    
    # Create white background
    background = np.ones((600, 600, 3), dtype=np.uint8) * 255
    
    # Paste the passport photo onto the white background
    background[0:600, 0:600] = passport_photo
    
    return background

def main():
    file_path = input("Please enter the path to your photo file: ")
    original_photo = load_image(file_path)
    
    if original_photo is not None:
        passport_photo = generate_passport_photo(original_photo)
        if passport_photo is not None:
            cv2.imshow('USCIS Passport Photo', passport_photo)
            output_path = 'uscis_passport_photo.jpg'
            cv2.imwrite(output_path, passport_photo)
            print(f"Passport photo saved as '{output_path}'")
            print("The photo is 600x750 pixels, which is 2x2.5 inches at 300 dpi.")
            cv2.waitKey(0)
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
