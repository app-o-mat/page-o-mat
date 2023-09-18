import os
from math import floor
import uuid
from pageomat.config import config_page_attribute
from pageomat.pages.color_utils import hex2red, hex2green, hex2blue
import qrcode

page_sizes = {
    "A3": (297, 420, "mm"),
    "A4": (210, 297, "mm"),
    "A5": (148, 210, "mm"),
    "Letter": (8.5, 11, "in"),
    "Tabloid": (11, 17, "in"),
    "Legal": (8.5, 14, "in"),
}


class Page:
    '''Base class for all pages'''
    def render_into(self, pdf):
        pass

    def page_width(self, config):
        page_size = config["page-size"]
        if type(page_size) is not str:
            return page_size["w"]
        return page_sizes[page_size][0]

    def page_height(self, config):
        page_size = config["page-size"]
        if type(page_size) is not str:
            return page_size["h"]
        return page_sizes[page_size][1]

    def page_unit(self, config):
        page_size = config["page-size"]
        if type(page_size) is not str:
            return page_size["unit"]
        return page_sizes[page_size][2]

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
        self.render_drawing(config, page, pdf)
        self.render_title(config, page, pdf)
        self.render_subtitle(config, page, pdf)
        self.render_footer(config, page, pdf)

    def render_title(self, config, page, pdf):
        if "title" not in page:
            return

        show_title = config_page_attribute(config, page, "show-title", True)
        if not show_title:
            return

        title = page["title"]

        font = config_page_attribute(config, page, "title-font", {"family": "Helvetica", "size": 16})
        pdf.set_font(font["family"], size=font["size"])
        color = config_page_attribute(config, page, "title-color", "#000")
        pdf.set_text_color(hex2red(color), hex2green(color), hex2blue(color))
        align = config_page_attribute(config, page, "title-align", "Left")
        pdf.cell(0, ln=0, txt=title, align=align[0].capitalize())

    def render_subtitle(self, config, page, pdf):
        if "subtitle" not in page:
            return
        show_title = config_page_attribute(config, page, "show-subtitle", True)
        if not show_title:
            return

        pdf.ln(0.4)
        subtitle = page["subtitle"]

        font = config_page_attribute(config, page, "subtitle-font", {"family": "Helvetica", "size": 12})
        pdf.set_font(font["family"], size=font["size"])
        color = config_page_attribute(config, page, "subtitle-color", "#000")
        pdf.set_text_color(hex2red(color), hex2green(color), hex2blue(color))
        align = config_page_attribute(config, page, "subtitle-align", "Left")
        pdf.cell(0, txt=subtitle, align=align[0].capitalize())

    def default_footer_offset(self, config):
        if self.page_unit(config) == "mm":
            return 2.5
        return 0.25

    def render_footer(self, config, page, pdf):
        footer = config_page_attribute(config, page, "footer", None)
        if footer is None:
            return

        footer = footer.replace("$page$", str(pdf.page_no()))
        footer_offset = config_page_attribute(config, page, "footer-offset", self.default_footer_offset(config))
        pdf.set_y(-footer_offset)

        font = config_page_attribute(config, page, "footer-font", {"family": "Helvetica", "size": 16})
        pdf.set_font(font["family"], size=font["size"])
        color = config_page_attribute(config, page, "footer-color", "#000")
        pdf.set_text_color(hex2red(color), hex2green(color), hex2blue(color))
        align = config_page_attribute(config, page, "footer-align", "Left")
        pdf.cell(0, txt=footer, align=align[0].capitalize())

    def render_rect(self, config, page, pdf, shape):
        pos = shape["pos"]
        size = shape["size"]
        fill = shape["fill"] if "fill" in shape else None
        stroke = shape["stroke"] if "stroke" in shape else None
        style = ""
        if stroke is not None:
            pdf.set_draw_color(hex2red(stroke), hex2green(stroke), hex2blue(stroke))
            style += "D"
        if fill is not None:
            pdf.set_fill_color(hex2red(fill), hex2green(fill), hex2blue(fill))
            style += "F"
        pdf.set_alpha(shape["alpha"] if "alpha" in shape else 1.0)
        pdf.rect(pos["x"], pos["y"], size["w"], size["h"], style=style)

    def render_line(self, config, page, pdf, shape):
        start = shape["start"]
        end = shape["end"]

        color = shape["color"] if "color" in shape else "#000"
        pdf.set_draw_color(hex2red(color), hex2green(color), hex2blue(color))

        line_width = shape["line-width"] if "line-width" in shape else 0.25
        pdf.set_line_width(line_width)
        pdf.line(start["x"], start["y"], end["x"], end["y"])

    def render_circle(self, config, page, pdf, shape):
        center = shape["center"]
        radius = shape["radius"]
        fill = shape["fill"] if "fill" in shape else None
        stroke = shape["stroke"] if "stroke" in shape else None
        style = ""
        if stroke is not None:
            pdf.set_draw_color(hex2red(stroke), hex2green(stroke), hex2blue(stroke))
            style += "D"
        if fill is not None:
            pdf.set_fill_color(hex2red(fill), hex2green(fill), hex2blue(fill))
            style += "F"
        pdf.set_alpha(shape["alpha"] if "alpha" in shape else 1.0)
        pdf.ellipse(center["x"] - radius, center["y"] - radius, radius * 2, radius * 2, style=style)

    def render_ellipse(self, config, page, pdf, shape):
        pos = shape["pos"]
        size = shape["size"]
        fill = shape["fill"] if "fill" in shape else None
        stroke = shape["stroke"] if "stroke" in shape else None
        style = ""
        if stroke is not None:
            pdf.set_draw_color(hex2red(stroke), hex2green(stroke), hex2blue(stroke))
            style += "D"
        if fill is not None:
            pdf.set_fill_color(hex2red(fill), hex2green(fill), hex2blue(fill))
            style += "F"
        pdf.set_alpha(shape["alpha"] if "alpha" in shape else 1.0)
        pdf.ellipse(pos["x"], pos["y"], size["w"], size["h"], style=style)

    def render_text(self, config, page, pdf, shape):
        pos = shape["pos"]
        size = shape["size"]
        text = shape["text"]
        align = shape["align"] if "align" in shape else "Left"

        color = shape["color"] if "color" in shape else None
        if color is not None:
            pdf.set_text_color(hex2red(color), hex2green(color), hex2blue(color))
        pdf.set_alpha(shape["alpha"] if "alpha" in shape else 1.0)
        pdf.set_xy(pos["x"], pos["y"])
        font = shape["font"] if "font" in shape else {"family": "Helvetica", "size": 16}
        pdf.set_font(font["family"], size=font["size"])
        pdf.multi_cell(w=size["w"], h=size["h"], txt=text, align=align[0].capitalize())

    def render_qr(self, config, page, pdf, shape):
        pos = shape["pos"]
        size = shape["size"]
        text = shape["text"]
        qr_image = qrcode.make(text)
        qr_filename = ".qr-tmp-" + str(uuid.uuid4()) + ".png"
        qr_image.save(qr_filename)
        pdf.image(qr_filename, pos["x"], pos["y"], size["w"], size["h"])
        if os.path.exists(qr_filename):
            os.remove(qr_filename)

    def render_drawing(self, config, page, pdf):
        if "drawing" not in page:
            return

        drawing = page["drawing"]
        for shape in drawing:
            if shape["type"] == "rect":
                self.render_rect(config, page, pdf, shape)
            elif shape["type"] == "line":
                self.render_line(config, page, pdf, shape)
            elif shape["type"] == "circle":
                self.render_circle(config, page, pdf, shape)
            elif shape["type"] == "ellipse":
                self.render_ellipse(config, page, pdf, shape)
            elif shape["type"] == "text":
                self.render_text(config, page, pdf, shape)
            elif shape["type"] == "qr":
                self.render_qr(config, page, pdf, shape)
            else:
                raise Exception("Unknown shape type: " + shape["type"])
            pdf.set_alpha(1.0)
