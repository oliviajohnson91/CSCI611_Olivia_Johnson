import cv2
import os

video_path = "runs/detect/predict4/traffic.avi"
output_dir = "runs/detect/predict4/video_frames"

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
frame_count = 0
saved = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_rate == 0: # save 1 frame per second
        filename = f"{output_dir}/frame_{saved:03d}.png"
        cv2.imwrite(filename, frame)
        saved += 1

    frame_count += 1

cap.release()
print("Saved", saved, "frames")