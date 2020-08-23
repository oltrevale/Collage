import cv2
import collage
"""
vid = cv2.VideoCapture("hes.mp4")
vid.set(cv2.CAP_PROP_POS_AVI_RATIO, 1)
print(vid.get(cv2.CAP_PROP_POS_MSEC))
num_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

for i in range(100, num_frames, 80):
    vid.set(1, i)
    ret, still = vid.read()
    cv2.imwrite(f'index{i}.jpg', still)"""

collage.create_collages()