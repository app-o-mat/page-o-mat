from pageomat.pages.page import Paper


def make_paper():
    return DotPaper()


class DotPaper(Paper):

    def render_into(self, config, paper, pdf):
        super().render_into(config, paper, pdf)
