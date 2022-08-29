from pageomat.pages.page import TemplatePage


def make_template():
    return SimpleTemplate()


class SimpleTemplate(TemplatePage):

    def render_into(self, config, page, pdf):
        super().render_into(config, page, pdf)
