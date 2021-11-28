import colorgram

class ColorImporter:

    def __init__(self):
        self.color_tuples = []

    def import_colors(self, image_file_name):
        colors = colorgram.extract(image_file_name, 40)
        self.color_tuples = []

        for color in colors:
            colorRgb = color.rgb
            r = colorRgb.r
            g = colorRgb.g
            b = colorRgb.b
            if r < 220 and g < 220 and b < 220:
                self.color_tuples.append((r, g, b))
        return self.color_tuples