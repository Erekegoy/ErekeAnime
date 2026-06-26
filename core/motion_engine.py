import cv2
import math


class MotionEngine:

    def __init__(self):
        self.max_zoom = 1.35

    def animate(self, image, frame_id, total_frames):

        h, w = image.shape[:2]

        t = frame_id / max(total_frames - 1, 1)

        zoom = 1.0 + (self.max_zoom - 1.0) * t

        zw = int(w * zoom)
        zh = int(h * zoom)

        frame = cv2.resize(image, (zw, zh))

        max_x = zw - w
        max_y = zh - h

        offset_x = int((math.sin(t * math.pi) * 0.5 + 0.5) * max_x)
        offset_y = int((math.cos(t * math.pi * 2) * 0.5 + 0.5) * max_y)

        frame = frame[
            offset_y:offset_y+h,
            offset_x:offset_x+w
        ]

        if frame.shape[:2] != (h, w):
            frame = cv2.resize(frame, (w, h))

        angle = math.sin(t * math.pi * 2) * 1.2

        matrix = cv2.getRotationMatrix2D(
            (w / 2, h / 2),
            angle,
            1.0
        )

        frame = cv2.warpAffine(
            frame,
            matrix,
            (w, h),
            borderMode=cv2.BORDER_REFLECT
        )

        return frame
