from datetime import datetime
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

        section_title = config_page_attribute(config, page, "section-title", None)

        section_font = config_page_attribute(config, page, "section-title-font", {"family": "Helvetica", "size": 10})
        pdf.set_font(section_font["family"], size=section_font["size"])
        section_color = config_page_attribute(config, page, "section-title-color", "#000")
        pdf.set_text_color(hex2red(section_color), hex2green(section_color), hex2blue(section_color))

        section_start_day_of_year = config_page_attribute(config, page, "section-start-day-of-year", None)
        section_end_day_of_year = config_page_attribute(config, page, "section-end-day-of-year", None)
        section_date_format = config_page_attribute(config, page, "section-date-format", "%y-%MM-%dd")
        year = config_page_attribute(config, page, "year", 2023)

        def write_section_title():
            nonlocal section_start_day_of_year
            nonlocal section_end_day_of_year
            nonlocal section
            title = section_title
            if section_title is not None:
                vars = {"__builtins__": None, "s": section}
                vars.update(page["indices"])
                if section_start_day_of_year is not None:
                    title = self.date_replace(title, "section-start-date", year, section_start_day_of_year, section_date_format, vars)
                if section_end_day_of_year is not None:
                    title = self.date_replace(title, "section-end-date", year, section_end_day_of_year, section_date_format, vars)

                pdf.text(10, yPos - spacing + grid_snap - 1, title)

        if section_count % 2 == 0:
            # If we have an even number of sections, then the
            # center line of the page will be the middle line.
            y_lines = floor((section_count - 1) / 2)
            for y in range(-y_lines, y_lines + 2):
                yPos = center_y + spacing * y
                if y < y_lines + 1:
                    pdf.line(0, yPos, width, yPos)

                section = y + y_lines  # 0 index
                if section < section_count:
                    write_section_title()
        else:
            # If we have an odd number of sections, then we'll
            # try to center the middle one around the center line of the page
            # But, if the grid-snap requires it, we'll snap to the closest
            # grid line.
            y_lines = floor(section_count / 2)
            for y in range(-y_lines, y_lines + 2):
                # We need to skip the 0 (no line in the center)
                if y != 0:
                    offset = (-spacing / 2 if y > 0 else spacing / 2) + grid_snap / 2
                    yPos = center_y + spacing * y + offset
                    if y < y_lines + 1:
                        pdf.line(0, yPos, width, yPos)

                    section = y + y_lines if y < 0 else y + y_lines - 1  # 0 index
                    write_section_title()

    def date_replace(self, title, key, year, day_of_year, date_format, vars):
        doy = day_of_year
        if type(day_of_year) is str:
            try:
                doy = eval(day_of_year, vars, {})
            except BaseException:
                print("Error evaluating: " + day_of_year)
                print("with variables " + str(vars))
                raise
        date = datetime.strptime(str(year) + "-" + str(doy), "%Y-%j")
        date_str = datetime.strftime(date, date_format)
        return title.replace("$" + key + "$", date_str)
