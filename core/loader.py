import os

SUPPORTED = (
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".bmp"
)


def load_images(folder="assets"):

    images = []

    if not os.path.isdir(folder):
        print(f"❌ Папка '{folder}' не найдена.")
        return images

    for root, _, files in os.walk(folder):

        for file in sorted(files):

            if file.lower().endswith(SUPPORTED):

                images.append(
                    os.path.join(root, file)
                )

    print(f"📚 Загружено страниц: {len(images)}")

    return images
