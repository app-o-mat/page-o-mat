from pageomat.pages.page import Page


def make_paper():
    return BlankPaper()


class BlankPaper(Page):

    def render_into(self, config, paper, pdf):
        super().render_into(config, paper, pdf)
