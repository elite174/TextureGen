from PIL import Image, ImageDraw

pixel_size = 3


def visualize(array, size, maxValue):
    K = 255 / maxValue
    img = Image.new('RGB', (size * pixel_size, size * pixel_size), (0, 0, 0))
    y = 0
    draw = ImageDraw.Draw(img)
    for i in range(size):
        x = 0
        for j in range(size):
            color = int(K * array[i][j])
            draw.rectangle([x, y, x + pixel_size, y + pixel_size], (color, color, color))
            x += pixel_size
        y += pixel_size
    img.save('map_bw.jpg', 'JPEG')
    del draw


def visualize_color_grad(array, size, maxValue):
    image = Image.open('grad.png')  # открываем картинку
    pix = image.load()
    print(image.size)

    def get_color_grad(value, maxValue):
        number = int((value / maxValue) * 1000)
        if number == 1000:
            number -= 1
        return (pix[number, 1][0], pix[number, 1][1], pix[number, 1][2])

    img = Image.new('RGB', (size * pixel_size, size * pixel_size), (0, 0, 0))
    y = 0
    draw = ImageDraw.Draw(img)
    for i in range(size):
        x = 0
        for j in range(size):
            draw.rectangle([x, y, x + pixel_size, y + pixel_size], get_color_grad(array[i][j], maxValue))
            x += pixel_size
        y += pixel_size
    img.save('map.jpg', 'JPEG')
    del draw
