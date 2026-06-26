import cv2
import os


def merge_videos(video_list, output_file):

    if len(video_list) == 0:
        return False

    first = cv2.VideoCapture(video_list[0])

    fps = first.get(cv2.CAP_PROP_FPS)

    width = int(first.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(first.get(cv2.CAP_PROP_FRAME_HEIGHT))

    first.release()

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    writer = cv2.VideoWriter(
        output_file,
        fourcc,
        fps,
        (width, height)
    )

    if not writer.isOpened():
        print("❌ Не удалось открыть VideoWriter")
        return False

    for video in video_list:

        cap = cv2.VideoCapture(video)

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            h, w = frame.shape[:2]

            if w != width or h != height:
                frame = cv2.resize(frame, (width, height))

            writer.write(frame)

        cap.release()

    writer.release()

    print(f"🎬 Финальное видео сохранено: {output_file}")

    return True
