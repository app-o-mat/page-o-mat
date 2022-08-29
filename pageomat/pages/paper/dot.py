from pageomat.pages.page import Page


def make_paper():
    return DotPaper()


class DotPaper(Page):

    def render_into(self, pdf):
        pass
