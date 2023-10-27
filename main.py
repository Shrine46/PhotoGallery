import os
import random
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from PIL import Image, ImageDraw
from kivy.uix.widget import Widget


class PhotoGalleryApp(App):
    pass

class Display(Screen, Widget):
    txtinput = ObjectProperty(None)
    button = ObjectProperty(None)
    image = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Display, self).__init__(**kwargs)
        self.index = 0

    def display_image(self, image):
        self.ids.main_image.source = image

    def inverse(self):
        image = self.ids.main_image.source
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = (225 - pixels[x, y][0])
                green = (225 - pixels[x, y][1])
                blue = (225 - pixels[x, y][2])
                pixels[x, y] = (red, green, blue)
        img.save("inv.png")
        self.display_image("inv.png")
        #self.ids.image_name.text = self.ids.main_image.source
    def black_and_white(self):
        image = self.ids.main_image.source
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                r, g, b = pixels[x, y]
                average = (r + g + b) // 3
                pixels[x, y] = (average, average, average)
        img.save("bw.png")
        self.display_image("bw.png")
        #self.ids.image_name.text = self.ids.main_image.source


    def edge_detection(self):
        image = self.ids.main_image.source
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if x < img.size[0] - 1:
                    total1 = pixels[x, y][0] + pixels[x, y][1] + pixels[x, y][2]
                    total2 = red2 = pixels[x - 1, y][0] + pixels[x - 1, y][1] + pixels[x - 1, y][2]
                    differance = abs(total1 - total2)
                    if differance > 5:
                        pixels[x - 1, y] = (0, 0, 0)
                    else:
                        pixels[x - 1, y] = (255, 255, 255)
        img.save("edge.png", flush=True)
        self.display_image("edge.png")
        #self.ids.image_name.text = self.ids.main_image.source
    def sepia(self):
        print()
        image = self.ids.main_image.source
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = int((pixels[x, y][0] * .393) + (pixels[x, y][1] * .769) + (pixels[x, y][2] * .189))
                green = int((pixels[x, y][0] * .349) + (pixels[x, y][1] * .686) + (pixels[x, y][2] * .168))
                blue = int((pixels[x, y][0] * .272) + (pixels[x, y][1] * .534) + (pixels[x, y][2] * .131))
                pixels[x, y] = (red, green, blue)
        img.save("sepi.png", flush=True)
        self.display_image("sepi.png")
        #self.ids.image_name.text = self.ids.main_image.source
    def pointillism(self):
        image = self.ids.main_image.source
        image = Image.open(image)
        canvas = Image.new("RGB", (image.size[0], image.size[1]), "white")
        pixels = image.load()
        for i in range(1000000):
            size2 = random.randint(5, 15)
            x = random.randint(0, image.size[0] - 10)
            y = random.randint(0, image.size[1] - 10)
            ellipsebox = [(x, y), (x + size2, y + size2)]
            draw = ImageDraw.Draw(canvas)
            draw.ellipse(ellipsebox, fill=(pixels[x, y][0], pixels[x, y][1], pixels[x, y][2]))
            del draw
        image.save("point.png", flush=True)
        self.display_image("point.png")
        #self.ids.image_name.text = self.ids.main_image.source

    # def pixelate(self, image, x, y, box_size=20, width=1, height=1):
    #     img = Image.open(image)
    #     pixels = img.load()
    #     for i in range(y, y + height, box_size):
    #         for j in range(x, x + width, box_size):
    #             red = 0
    #             green = 0
    #             blue = 0
    #             count = 0
    #             for y1 in range(i, min(i + box_size, img.height)):
    #                 for x1 in range(j, min(j + box_size, img.width)):
    #                     r, g, b = (pixels[x1, y1])
    #                     count += 1
    #                     red += r
    #                     green += g
    #                     blue += b
    #             avg_red = int(red / count)
    #             avg_green = int(green / count)
    #             avg_blue = int(blue / count)
    #             for y1 in range(i, min(i + box_size, img.height)):
    #                 for x1 in range(j, min(j + box_size, img.width)):
    #                     pixels[x1, y1] = (avg_red, avg_green, avg_blue)
    #     img.save("pixelated.png")
    #     self.display_image("pixelated")

PhotoGalleryApp().run()