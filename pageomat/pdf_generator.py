from importlib import import_module
from fpdf import FPDF
from pageomat.config import config_attribute, config_page_attribute


class PdfGenerator:

    config = None

    def __init__(self, config):
        self.config = config

    def num_pages(self):
        return len(self.pages())

    def pages(self):
        '''Returns a flattened array of the pages'''
        return self.pages_from_subpages(self.config["pages"])

    def page_size(self):
        if "page-size" in self.config:
            return self.config["page-size"]
        return "A5"

    def page_unit(self):
        size = self.page_size()
        if size.startswith("A"):
            return "mm"
        return "in"

    def make_pdf(self, filename):
        pdf = FPDF(format=self.page_size(), unit=self.page_unit())
        pdf.set_auto_page_break(False)
        pdf.set_author(config_attribute(self.config, "pdf-author", "Page-o-Mat"))
        pdf.set_title(config_attribute(self.config, "pdf-title", "Page-o-Mat Journal"))
        for page in self.pages():
            pdf.add_page()
            self.render_paper(page, pdf)
            self.render_template(page, pdf)

        pdf.output(filename)

    def render_paper(self, page, pdf):
        paper_module_name = self.module_for_paper(page)
        paper_module = import_module(paper_module_name)
        paper = paper_module.make_paper()
        paper.render_into(self.config, self.paper_definition(page), pdf)

    def render_template(self, page, pdf):
        template_module_name = self.module_for_template(page)
        template_module = import_module(template_module_name)
        pdf_page = template_module.make_template()
        pdf_page.render_into(self.config, page, pdf)

    def page_attribute(self, page, key, default_value):
        return config_page_attribute(self.config, page, key, default_value)

    def paper_definition(self, page):
        return self.page_attribute(page, "paper", {"type": "blank"})

    def module_for_paper(self, page):
        module = "pageomat.pages.paper." + self.paper_definition(page)["type"]
        return module.replace("-", "_")

    def module_for_template(self, page):
        module = "pageomat.pages.template." + self.page_attribute(page, "type", "simple")
        return module.replace("-", "_")

    def pages_from_subpages(self, pages):
        result = []
        for p in pages:
            count = 1
            if "count" in p:
                count = p["count"]

            variants = [None]
            if "variants" in p:
                variants = p["variants"]

            for v in variants:
                for _ in range(0, count):
                    if "pages" in p:
                        result = result + self.pages_from_subpages(p["pages"])
                    else:
                        result.append(self.flatten_page(p, v))

        return result

    def include_for_flatten(self, key):
        return key not in {"count", "variants", "pages"}

    def flatten_page(self, page, variant):
        result = {k: page[k] for k in filter(self.include_for_flatten, page.keys())}

        if variant is not None:
            result["variant"] = variant

        return result
