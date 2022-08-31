from datetime import datetime
from importlib import import_module
from fpdf import FPDF
from pageomat.config import config_attribute, config_page_attribute
from pageomat.pages.page import page_sizes


class PdfGenerator:

    config = None

    def __init__(self, config):
        self.config = config

    def num_pages(self):
        return len(self.pages())

    def pages(self, include_indices=False):
        '''Returns a flattened array of the pages'''
        return self.pages_from_subpages(self.config["pages"], include_indices=include_indices)

    def page_size(self):
        if "page-size" in self.config:
            return self.config["page-size"]
        return "A5"

    def page_unit(self):
        return page_sizes[self.page_size()][2]

    def make_pdf(self, filename):
        pdf = FPDF(format=self.page_size(), unit=self.page_unit())
        pdf.set_auto_page_break(False)
        pdf.set_author(config_attribute(self.config, "pdf-author", "Page-o-Mat"))
        pdf.set_title(config_attribute(self.config, "pdf-title", "Page-o-Mat Journal"))
        for page in self.pages(include_indices=True):
            top_margin = config_page_attribute(self.config, page, "top-margin", None)
            if top_margin is not None:
                pdf.set_top_margin(top_margin)
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

    def pages_from_subpages(self, pages, page_start=0, parent_variant=None, include_indices=False, parent_count=[]):
        result = []
        for p in pages:
            count = 1
            if "count" in p:
                count = p["count"]

            variants = [None]
            if "variants" in p:
                variants = p["variants"]

            for vIndex, v in enumerate(variants):
                for c in range(0, count):
                    if "pages" in p:
                        result = result + self.pages_from_subpages(
                            p["pages"],
                            parent_variant=v if v is not None else parent_variant,
                            include_indices=include_indices,
                            parent_count=parent_count + [c],
                            page_start=len(result))
                    else:
                        page = self.flatten_page(p, v, parent_variant)
                        if include_indices:
                            page["indices"] = {
                                "p": len(result) + page_start,
                                "c": parent_count + [c],
                                "v": vIndex
                            }
                        result.append(page)

        return result

    def include_for_flatten(self, key):
        return key not in {"count", "variants", "pages"}

    def flatten_page(self, page, variant, parent_variant):
        if variant is not None:
            if parent_variant is not None:
                variant = variant.replace("$variant$", parent_variant)
        elif parent_variant is not None:
            variant = parent_variant

        result = {k: page[k] for k in filter(self.include_for_flatten, page.keys())}

        year = config_page_attribute(self.config, page, "year", None)
        if year is not None:
            day_of_year = config_page_attribute(self.config, page, "day-of-year", 1)
            date_format = config_page_attribute(self.config, page, "date-format", "%y-%MM-%dd")
            date = datetime.strptime(str(year) + "-" + str(day_of_year), "%Y-%j")
            result["date"] = datetime.strftime(date, date_format)

        if variant is not None:
            result["variant"] = variant

        result = {k: self.substitute_variables(result[k], result) for k in result.keys()}

        return result

    def substitute_variables(self, value, page):
        if type(value) is not str:
            return value

        if "variant" in page and page["variant"] is not None:
            value = value.replace("$variant$", page["variant"])

        if "date" in page:
            value = value.replace("$date$", page["date"])

        return value
