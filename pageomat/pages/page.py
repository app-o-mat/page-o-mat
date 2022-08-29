from pageomat.config import config_page_attribute
from pageomat.pages.color_utils import hex2red, hex2green, hex2blue


class Page:
    '''Base class for all pages'''
    def render_into(self, pdf):
        pass


class Paper(Page):
    '''Base class for paper'''
    def render_into(self, config, paper, pdf):
        super().render_into(pdf)


class TemplatePage(Page):
    '''Base class for templates'''
    def render_into(self, config, page, pdf):
        super().render_into(pdf)
        self.render_title(config, page, pdf)

    def render_title(self, config, page, pdf):
        if "title" not in page:
            return

        font = config_page_attribute(config, page, "title-font", {"family": "Helvetica", "size": 16})
        pdf.set_font(font["family"], size=font["size"])
        color = config_page_attribute(config, page, "title-color", "#000")
        pdf.set_text_color(hex2red(color), hex2green(color), hex2blue(color))
        pdf.cell(0, txt=page["title"])
