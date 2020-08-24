from PIL import Image


def create_collages(listofimages, width, height):
    cols = 10
    rows = 10
    width = width * 10
    height = height * 10
    thumbnail_width = int(width / cols)
    thumbnail_height = int(height / rows)
    new_im = Image.new('RGB', (width, height))
    ims = []
    for p in listofimages:
        im = Image.open(p)
        ims.append(im)
    print(ims)
    i = 0
    x = 0
    y = 0
    for col in range(cols):
        for row in range(rows):
            print(i, x, y)
            new_im.paste(ims[i], (x, y))
            i += 1
            y += thumbnail_height
        x += thumbnail_width
        y = 0

    new_im.save("Collage.jpg")
    print("fatto")
