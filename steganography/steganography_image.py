#  External dependencies
import numpy as np
import json
import zlib
from PIL import Image
import base64
import re
import copy

class Payload:

    def __init__(self, rawData=None, json_str=None):
        self.compression_level = 9
        if rawData:
            self.rawData = rawData
            self.create_json()
        elif json_str:
            self.json = json.loads(json_str)
            self.extract_data()

    def create_json(self):
        payload_json = {
            "type":"text",
            "size":0,
            "content":"",
        }

        payload_json["size"] = len(self.rawData)
        compressed_content = zlib.compress(self.rawData.encode(), self.compression_level)
        compressed_content = base64.b64encode(compressed_content)
        payload_json["content"] = str(compressed_content).split("'")[1]
        self.json = json.dumps(payload_json)

    def extract_data(self):
        compressed_content = self.json["content"]
        decompressed_content = base64.b64decode(compressed_content)
        decompressed_content = zlib.decompress(decompressed_content)
        self.rawData = decompressed_content.decode()


class Carrier: 
    def __init__(self, img): 
        if (img):
            self.img = Image.open(img).convert('RGBA')
            self.img = np.asarray(self.img)
            self.size = {"height":len(self.img), "width":len(self.img[0])}

    def payloadExists(self):
        copied_image = copy.deepcopy(self.img)
        copied_image = copied_image.flatten()

        check_first = copied_image[0:4]
        check_second = copied_image[4:8]
        check_third = copied_image[8:12]
        check_pixels = [check_first, check_second, check_third]
        pixel_string = []

        for pixel in check_pixels:
            temp_pixel = []
            for color in pixel:
                temp_color =  '{0:08b}'.format(color)
                temp_color = temp_color[6:8]
                temp_pixel.append(temp_color)
            temp_pixel = ''.join(temp_pixel)
            temp_pixel = int(temp_pixel, 2)
            temp_pixel = chr(temp_pixel)
            pixel_string.append(temp_pixel)

        if pixel_string[0] == "{" and pixel_string[1] == '"' and pixel_string[2] == "t":
            return True


    def clean(self):
        bin_array = []

        copied_image = copy.deepcopy(self.img)
        copied_image = copied_image.flatten()
        clean_image = []

        for color in copied_image:
            pixel_part = list('{0:08b}'.format(color))
            pixel_part[6:8] = ["0", "0"]
            clean_image.append(int(''.join(pixel_part), 2))

        self.img = np.resize(clean_image, (self.size["height"], self.size["width"], 4))
    
    def embed_payload(self, payload):
        if self.payloadExists():
            self.extract_payload()
            self.clean()

        bin_array = []
        for ind_char in (payload.json):
            temp_bin = '{0:08b}'.format(ord(ind_char), 'b')
            bin_array.append(temp_bin[0:2])
            bin_array.append(temp_bin[2:4])
            bin_array.append(temp_bin[4:6])
            bin_array.append(temp_bin[6:8])

        copied_image = copy.deepcopy(self.img)
        copied_image = copied_image.flatten()

        for i in range(len(bin_array)):
            pixel_part = list('{0:08b}'.format(copied_image[i]))
            pixel_part[6:8] = bin_array[i]
            copied_image[i] = int(''.join(pixel_part), 2)

        self.img = np.resize(copied_image, (self.size["height"], self.size["width"], 4))
    
    def extract_payload(self):
        if self.payloadExists():
            copied_image = copy.deepcopy(self.img)
            pixel_string = []

            breakFlag = 0

            for row in copied_image:
                if breakFlag:
                    break

                for pixel in row:
                    if breakFlag:
                        break

                    temp_pixel = []
                    for color in pixel:
                        temp_color =  '{0:08b}'.format(color)
                        temp_color = temp_color[6:8]
                        temp_pixel.append(temp_color)
                    temp_pixel = ''.join(temp_pixel)
                    temp_pixel = int(temp_pixel, 2)
                    temp_pixel = chr(temp_pixel)
                    pixel_string.append(temp_pixel)
                    if pixel_string[-1] == "}" and pixel_string[-2] == '"':
                        breakFlag = 1
                        break
            self.payload = ''.join(pixel_string)

            return self.payload
        else:
            return False
        