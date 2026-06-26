import os

SUPPORTED = (".png", ".jpg", ".jpeg", ".webp")


def load_images(folder="assets"):
    images = []

    if not os.path.exists(folder):
        return images

    for file in sorted(os.listdir(folder)):
        if file.lower().endswith(SUPPORTED):
            images.append(os.path.join(folder, file))

    return images

