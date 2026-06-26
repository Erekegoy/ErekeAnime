import cv2


def read_image(path):
    image = cv2.imread(path)

    if image is None:
        return None

    height, width = image.shape[:2]

    return {
        "path": path,
        "width": width,
        "height": height,
        "image": image
    }	

