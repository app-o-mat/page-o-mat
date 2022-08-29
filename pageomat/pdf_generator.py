class PdfGenerator:

    config = None

    def __init__(self, config):
        self.config = config

    def num_pages(self):
        return len(self.pages())

    def pages(self):
        '''Returns a flattened array of the pages'''
        pages = self.config["pages"]
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
                    flattened_page = {
                        "type": p["type"]
                    }
                    if v is not None:
                        flattened_page["variant"] = v
                    result.append(flattened_page)

        return result
