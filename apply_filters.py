from PIL import Image


def convert_to_bw(img):
    return img.convert('L')


def resize(img):
    size = 300, 300
    img.thumbnail(size, Image.ANTIALIAS)
    return img


def flip(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)


def concat(img):
    # https://note.nkmk.me/en/python-pillow-concat-images/
    pass


def main():
    im = Image.open("zombie.png")
    im_out = resize(im)
    im_out = convert_to_bw(im_out)
    im_out = flip(im_out)
    im.show()
    im_out.show()


if __name__ == '__main__':
    main()
