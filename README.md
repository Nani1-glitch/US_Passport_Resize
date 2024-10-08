# 📸 Passport Photo Generator

![Project License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python](https://img.shields.io/badge/python-v3.7%2B-blue) ![opencv](https://img.shields.io/badge/OpenCV-4.x-green)

## 🌟 Overview

This Python project allows users to generate passport photos from any image with a visible face. The script detects the face, crops the image, and formats it to match the standard passport photo dimensions. It's simple, efficient, and leverages OpenCV for image processing.

## ⚙️ Features

- 👤 **Face Detection**: Automatically detects faces using OpenCV's Haar Cascade Classifier.
- ✂️ **Cropping & Resizing**: Crops the detected face and resizes it to standard passport photo dimensions (600x600 pixels).
- 📐 **Aspect Ratio Maintenance**: Ensures the photo adheres to a 2x2 inch (51x51 mm) format for passport photos.
- 🖼️ **White Background**: Applies a clean white background to the processed image for professional output.

## 🛠️ Installation

Ensure you have Python and the required libraries installed:

```bash
pip install numpy opencv-python

# 🚀 Usage

Clone this repository:

```bash
git clone https://github.com/yourusername/passport-photo-generator.git
cd passport-photo-generator

Input the file path of the image you want to process.

The script will generate a passport photo and display it.

## 📸 Example

Here’s an example of how the tool works:

### Input Image:
- The original image should contain a clear face.

### Output Passport Photo:
- The processed passport photo with the correct dimensions and background will be displayed.

## 🧑‍💻 Code Overview

### Functions:
- `load_image(file_path)`: Loads the image from the specified file path.
- `generate_passport_photo(image)`: Detects a face in the image, crops and resizes it, and generates a passport-sized photo.
- `main()`: Prompts the user for input and processes the image accordingly.

## 📚 Libraries Used

- **OpenCV**: For image manipulation and face detection.
- **NumPy**: For efficient matrix operations.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributions

Feel free to open issues or submit pull requests. Any contributions are welcome!

## 📧 Contact

If you have any questions, feel free to reach out:

- **Your Name**: [Email](mailto:nithinrajulapati9999@gmail.com)
- **GitHub**: [Your GitHub Profile]([https://github.com/yourusername](https://github.com/Nani1-glitch))
