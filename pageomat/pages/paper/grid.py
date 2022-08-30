from math import floor
from pageomat.pages.color_utils import hex2blue, hex2green, hex2red
from pageomat.pages.page import Paper


def make_paper():
    return GridPaper()


class GridPaper(Paper):

    def render_into(self, config, paper, pdf):
        super().render_into(config, paper, pdf)
        width = self.page_width(config)
        height = self.page_height(config)
        line_width = self.paper_attribute(paper, "line-width", 0.25)

        spacing = self.paper_attribute(paper, "spacing", 5)

        center_x = width / 2
        x_lines = floor(center_x / spacing)
        center_y = height / 2
        y_lines = floor(center_y / spacing)

        color = self.paper_attribute(paper, "color", "#000")
        pdf.set_draw_color(hex2red(color), hex2green(color), hex2blue(color))
        pdf.set_line_width(line_width)
        for x in range(-x_lines, x_lines + 1):
            pdf.line(
                center_x + spacing * x, 0,
                center_x + spacing * x, height)

        for y in range(-y_lines, y_lines + 1):
            pdf.line(
                0, center_y + spacing * y,
                width, center_y + spacing * y)
