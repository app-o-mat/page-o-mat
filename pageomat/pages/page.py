from math import floor
from pageomat.config import config_page_attribute
from pageomat.pages.color_utils import hex2red, hex2green, hex2blue


page_sizes = {
    "A3": (297, 420, "mm"),
    "A4": (210, 297, "mm"),
    "A5": (148, 210, "mm"),
    "Letter": (8.5, 11, "in"),
    "Legal": (8.5, 14, "in"),
}


class Page:
    '''Base class for all pages'''
    def render_into(self, pdf):
        pass

    def page_width(self, config):
        page_size = config["page-size"]
        return page_sizes[page_size][0]

    def page_height(self, config):
        page_size = config["page-size"]
        return page_sizes[page_size][1]

    def grid_snap_value(self, grid_snap, value):
        if grid_snap > 0:
            return floor(value / grid_snap) * grid_snap
        return value


class Paper(Page):
    '''Base class for paper'''
    def render_into(self, config, paper, pdf):
        super().render_into(pdf)

    def paper_attribute(self, paper, key, default_value):
        if key in paper:
            return paper[key]
        return default_value


class TemplatePage(Page):
    '''Base class for templates'''
    def render_into(self, config, page, pdf):
        super().render_into(pdf)
        top_margin = config_page_attribute(config, page, "top-margin", None)
        if top_margin is not None:
            pdf.set_top_margin(top_margin)
        self.render_title(config, page, pdf)
        self.render_footer(config, page, pdf)

    def render_title(self, config, page, pdf):
        if "title" not in page:
            return

        title = page["title"]

        font = config_page_attribute(config, page, "title-font", {"family": "Helvetica", "size": 16})
        pdf.set_font(font["family"], size=font["size"])
        color = config_page_attribute(config, page, "title-color", "#000")
        pdf.set_text_color(hex2red(color), hex2green(color), hex2blue(color))
        align = config_page_attribute(config, page, "title-align", "Left")
        pdf.cell(0, txt=title, align=align[0].capitalize())

    def render_footer(self, config, page, pdf):
        footer = config_page_attribute(config, page, "footer", None)
        if footer is None:
            return

        footer = footer.replace("$page$", str(pdf.page_no()))
        footer_offset = config_page_attribute(config, page, "footer-offset", 2.5)
        pdf.set_y(-footer_offset)

        font = config_page_attribute(config, page, "footer-font", {"family": "Helvetica", "size": 16})
        pdf.set_font(font["family"], size=font["size"])
        color = config_page_attribute(config, page, "footer-color", "#000")
        pdf.set_text_color(hex2red(color), hex2green(color), hex2blue(color))
        align = config_page_attribute(config, page, "footer-align", "Left")
        pdf.cell(0, txt=footer, align=align[0].capitalize())
