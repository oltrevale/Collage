from PIL import Image


def create_collages(listofimages, width, height):
    #todo cols and rows dipenderanno dal numero di frame che serviranno
    cols = 20
    rows = 20
    width = width * 20
    height = height * 20
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
    for row in range(rows):
        for col in range(cols):
            print(i, x, y)
            new_im.paste(ims[i], (x, y))
            i += 1
            x += thumbnail_width
        y += thumbnail_height
        x = 0

    new_im.save("Collage.jpg")
    print("fatto")
