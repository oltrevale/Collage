import cv2
import collage
import sys

vid = cv2.VideoCapture(sys.argv[1])
vid.set(cv2.CAP_PROP_POS_AVI_RATIO, 1)

num_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
#todo trovare un algoritmo per cercare il numero di frame ci servono in base alla lunghezza del video
chunk = int(num_frames / 401)
list_images = []
for i in range(chunk, num_frames - chunk, chunk):
    vid.set(1, i)
    ret, still = vid.read()
    cv2.imwrite(f'index{i}.jpg', still)
    list_images.append(f'index{i}.jpg')
collage.create_collages(list_images, int(width), int(height))
