import cv2
import os

from core.motion_engine import MotionEngine


motion = MotionEngine()


def animate_panel(panel_path, output_video, seconds=5, fps=30):

    image = cv2.imread(panel_path)

    if image is None:
        print("Ошибка чтения:", panel_path)
        return False

    h, w = image.shape[:2]

    os.makedirs(os.path.dirname(output_video), exist_ok=True)

    writer = cv2.VideoWriter(
        output_video,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (w, h)
    )

    if not writer.isOpened():
        print("Не удалось создать видео")
        return False

    total_frames = seconds * fps

    for frame_id in range(total_frames):

        frame = motion.animate(
            image,
            frame_id,
            total_frames
        )

        writer.write(frame)

    writer.release()

    return True
