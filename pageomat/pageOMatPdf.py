from fpdf import FPDF


# This code comes from https://stackoverflow.com/a/63041654/3937
# It is licensed under CC BY-SA 4.0
class PageOMatPdf(FPDF):
    def __init__(self, orientation='P', unit='mm', format='A4'):
        self.__extgstates = []
        super().__init__(orientation, unit, format)

    # alpha: real value from 0 (transparent) to 1 (opaque)
    # bm:    blend mode, one of the following:
    #          Normal, Multiply, Screen, Overlay, Darken, Lighten, ColorDodge, ColorBurn,
    #          HardLight, SoftLight, Difference, Exclusion, Hue, Saturation, Color, Luminosity
    def set_alpha(self, alpha, bm='Normal'):
        # set alpha for stroking (CA) and non-stroking (ca) operations
        data = {'ca': alpha, 'CA': alpha, 'BM': '/' + bm, 'n': 0}
        gs = self.add_ext_gstate(data)
        self.set_ext_gstate(gs + 1)

    def add_ext_gstate(self, data):
        n = len(self.__extgstates)
        self.__extgstates.append(data)
        return n

    def _enddoc(self):
        if len(self.__extgstates) > 0 and self.pdf_version < '1.4':
            self.pdf_version = '1.4'
        super()._enddoc()

    def set_ext_gstate(self, gs):
        self._out('/GS%d gs' % (gs))

    def _putextgstates(self):
        i = 0
        while i < len(self.__extgstates):
            self._newobj()
            self._out('<</Type /ExtGState')
            self.__extgstates[i]["n"] = self.n
            parms = self.__extgstates[i]
            self._out('/ca %.3F' % (parms["ca"]))
            self._out('/CA %.3F' % (parms["CA"]))
            self._out('/BM ' + parms["BM"])
            self._out('>>')
            self._out('endobj')
            i += 1

    def _putresourcedict(self):
        super()._putresourcedict()
        self._out('/ExtGState <<')
        for index, eg in enumerate(self.__extgstates):
            self._out('/GS' + str(index + 1) + ' ' + str(eg["n"]) + ' 0 R')
        self._out('>>')

    def _putresources(self):
        self._putextgstates()
        super()._putresources()
