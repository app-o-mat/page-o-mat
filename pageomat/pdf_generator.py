class PdfGenerator:

    config = None

    def __init__(self, config):
        self.config = config

    def num_pages(self):
        pages = self.config["pages"]
        result = 0
        for p in pages:
            if "count" in p:
                result += p["count"]
            else:
                result += 1

            variant_count = 1
            if "variants" in p:
                variant_count = len(p["variants"])
            result *= variant_count

        return result
