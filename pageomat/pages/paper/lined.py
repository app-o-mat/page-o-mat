from math import floor
from pageomat.pages.color_utils import hex2blue, hex2green, hex2red
from pageomat.pages.page import Paper


def make_paper():
    return LinedPaper()


class LinedPaper(Paper):

    def render_into(self, config, paper, pdf):
        super().render_into(config, paper, pdf)
        width = self.page_width(config)
        height = self.page_height(config)
        line_width = self.paper_attribute(paper, "line-width", 0.25)

        # Support both names "heading" (old) and "header-space" (new)
        header_space = self.paper_attribute(paper, "heading", 0)
        header_space = self.paper_attribute(paper, "header-space", header_space)

        spacing = self.paper_attribute(paper, "spacing", 5)

        center_y = height / 2
        y_lines = floor(center_y / spacing)

        color = self.paper_attribute(paper, "color", "#000")
        pdf.set_draw_color(hex2red(color), hex2green(color), hex2blue(color))
        pdf.set_line_width(line_width)

        for y in range(-y_lines, y_lines + 1):
            y_pos = center_y + spacing * y
            if y_pos >= heading:
                pdf.line(0, y_pos, width, y_pos)
