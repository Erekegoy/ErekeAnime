import cv2
import os


def animate_panel(panel_path, output_video, seconds=4, fps=30):

    image = cv2.imread(panel_path)

    if image is None:
        print("Ошибка чтения:", panel_path)
        return False

    h, w = image.shape[:2]

    os.makedirs(os.path.dirname(output_video), exist_ok=True)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    writer = cv2.VideoWriter(
        output_video,
        fourcc,
        fps,
        (w, h)
    )

    if not writer.isOpened():
        print("Не удалось создать видео")
        return False

    total_frames = seconds * fps

    max_zoom = 1.25

    for i in range(total_frames):

        t = i / (total_frames - 1)

        scale = 1.0 + (max_zoom - 1.0) * t

        new_w = int(w * scale)
        new_h = int(h * scale)

        zoom = cv2.resize(image, (new_w, new_h))

        max_x = new_w - w
        max_y = new_h - h

        offset_x = int(max_x * t)
        offset_y = int(max_y * (1.0 - t))

        frame = zoom[
            offset_y:offset_y + h,
            offset_x:offset_x + w
        ]

        if frame.shape[0] != h or frame.shape[1] != w:
            frame = cv2.resize(frame, (w, h))

        writer.write(frame)

    writer.release()

    return True
