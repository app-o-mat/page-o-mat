class PdfGenerator:

    config = None

    def __init__(self, config):
        self.config = config

    def num_pages(self):
        return len(self.pages())

    def pages(self):
        '''Returns a flattened array of the pages'''
        return self.pages_from_subpages(self.config["pages"])

    def module_for_paper(self, page):
        paper_prefix = "pageomat.pages.paper."
        if "paper" in page:
            return paper_prefix + page["paper"]["type"]
        elif "defaults" in self.config and "paper" in self.config["defaults"]:
            return paper_prefix + self.config["defaults"]["paper"]["type"]
        else:
            return paper_prefix + "blank"

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
