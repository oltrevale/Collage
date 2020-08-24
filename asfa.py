import cv2
import collage
import sys


vid = cv2.VideoCapture(sys.argv[1])
vid.set(cv2.CAP_PROP_POS_AVI_RATIO, 1)
print(vid.get(cv2.CAP_PROP_POS_MSEC))
num_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
chunk = int(num_frames / 7)
listofimages = []
for i in range(chunk, num_frames - chunk, chunk):
    vid.set(1, i)
    ret, still = vid.read()
    cv2.imwrite(f'index{i}.jpg', still)
    listofimages.append(f'index{i}.jpg')

collage.create_collages(listofimages)