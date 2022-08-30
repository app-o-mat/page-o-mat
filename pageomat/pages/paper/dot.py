from math import floor
from pageomat.pages.color_utils import hex2blue, hex2green, hex2red
from pageomat.pages.page import Paper


def make_paper():
    return DotPaper()


class DotPaper(Paper):

    def render_into(self, config, paper, pdf):
        super().render_into(config, paper, pdf)
        width = self.page_width(config)
        height = self.page_height(config)
        dot_size = self.paper_attribute(paper, "dot-size", 0.5)
        dot_offset = dot_size / 2

        spacing = self.paper_attribute(paper, "spacing", 5)

        center_x = width / 2
        x_dots = floor(center_x / spacing)
        center_y = height / 2
        y_dots = floor(center_y / spacing)

        color = self.paper_attribute(paper, "color", "#000")
        pdf.set_fill_color(hex2red(color), hex2green(color), hex2blue(color))
        for x in range(-x_dots, x_dots + 1):
            for y in range(-y_dots, y_dots + 1):
                pdf.ellipse(
                    center_x - dot_offset + spacing * x,
                    center_y - dot_offset + spacing * y,
                    dot_size, dot_size, 'F')
