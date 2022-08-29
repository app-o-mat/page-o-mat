from pageomat.pages.page import TemplatePage


def make_template():
    return HorizontalSplitTemplate()


class HorizontalSplitTemplate(TemplatePage):

    def render_into(self, config, page, pdf):
        super().render_into(config, page, pdf)
