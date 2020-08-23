from PIL import Image


def create_collages():
    listofimages = ['index100.jpg', 'index180.jpg', "index260.jpg", 'index340.jpg', 'index420.jpg', 'index500.jpg']
    cols = 3
    rows = 2
    width = 5760
    height = 1080 * 2
    thumbnail_width = width // cols
    thumbnail_height = height // rows
    size = thumbnail_width, thumbnail_height
    new_im = Image.new('RGB', (width, height))
    ims = []
    for p in listofimages:
        im = Image.open(p)
        im.thumbnail(size)
        ims.append(im)
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
