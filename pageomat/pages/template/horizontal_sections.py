from math import floor
from pageomat.config import config_page_attribute
from pageomat.pages.color_utils import hex2blue, hex2green, hex2red
from pageomat.pages.page import TemplatePage


def make_template():
    return HorizontalSectionsTemplate()


class HorizontalSectionsTemplate(TemplatePage):

    def render_into(self, config, page, pdf):
        super().render_into(config, page, pdf)

        width = self.page_width(config)
        height = self.page_height(config)
        center_y = height / 2
        section_count = config_page_attribute(config, page, "section-count", 2)
        line_width = config_page_attribute(config, page, "line-width", 0.2)
        line_color = config_page_attribute(config, page, "line-color", "#000")

        pdf.set_draw_color(hex2red(line_color), hex2green(line_color), hex2blue(line_color))
        pdf.set_line_width(line_width)

        grid_snap = config_page_attribute(config, page, "grid-snap", 0)
        spacing = self.grid_snap_value(grid_snap, height / section_count)

        if section_count % 2 == 0:
            # If we have an even number of sections, then the
            # center line of the page will be the middle line.

            y_lines = floor((section_count - 1) / 2)
            for y in range(-y_lines, y_lines + 1):
                pdf.line(
                    0, center_y + spacing * y,
                    width, center_y + spacing * y)
        else:
            # If we have an odd number of sections, then we'll
            # try to center the middle one around the center line of the page
            # But, if the grid-snap requires it, we'll snap to the closest
            # grid line.
            y_lines = floor((section_count - 1) / 2)
            for y in range(-y_lines, y_lines + 1):
                # We need to skip the 0 (no line in the center)
                if y != 0:
                    offset = (-spacing / 2 if y > 0 else spacing / 2) + grid_snap / 2
                    pdf.line(
                        0, center_y + spacing * y + offset,
                        width, center_y + spacing * y + offset)
