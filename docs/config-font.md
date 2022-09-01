# Page-o-Mat Configuration: font keys

|key|Example|Description|
|---|-------|-----------|
|family|Helvetica|The font-family to use.|
|size|16|The size of the font in points|

If you use Latin 1 PDF fonts (Helvetica, Times, Symbol, Courier, or Zapfdingbats), then you may not need to embed them.

If you use other fonts, you need to have a TTF file for the font and use the `embed-fonts` key to make them available to the PDF (see [embed-fonts](config-embed-fonts.md)).