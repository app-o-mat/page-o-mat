from pageomat.pages.page import Page


def make_paper():
    return BlankPaper()


class BlankPaper(Page):

    def render_into(self, pdf):
        pass
