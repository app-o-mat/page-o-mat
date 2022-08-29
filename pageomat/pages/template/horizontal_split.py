from pageomat.pages.page import Page


def make_template():
    return HorizontalSplitTemplate()


class HorizontalSplitTemplate(Page):

    def render_into(self, pdf):
        pass
