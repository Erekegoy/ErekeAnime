import cv2
import os


def preprocess_image(input_path, output_dir="outputs"):
    image = cv2.imread(input_path)

    if image is None:
        return False

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    filename = os.path.basename(input_path)
    output_path = os.path.join(output_dir, f"gray_{filename}")

    cv2.imwrite(output_path, gray)

    return output_path
