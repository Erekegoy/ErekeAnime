import cv2
import os


def detect_panels(image_path, output_dir="outputs/panels"):
    os.makedirs(output_dir, exist_ok=True)

    image = cv2.imread(image_path)

    if image is None:
        return []

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blur, 50, 150)

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    panels = []
    index = 1

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        # Игнорируем слишком маленькие области
        if w < 100 or h < 100:
            continue

        crop = image[y:y+h, x:x+w]

        filename = f"panel_{index}.jpg"
        path = os.path.join(output_dir, filename)

        cv2.imwrite(path, crop)

        panels.append(path)
        index += 1

    return panels
