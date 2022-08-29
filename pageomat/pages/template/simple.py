from pageomat.pages.page import Page


def make_template():
    return SimpleTemplate()


class SimpleTemplate(Page):

    def render_into(self, pdf):
        pass
