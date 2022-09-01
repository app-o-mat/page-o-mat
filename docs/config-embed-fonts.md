# Page-o-Mat Configuration: Embedded fonts

If you use a non-Latin 1 PDF font, then you will need to embed it in the PDF. You can use the top-level `embed-fonts` key to do that.

Example (on a Mac):

```yaml
page-size: A5
embed-fonts:
- family: Monaco
  fname: /System/Library/Fonts/Monaco.ttf
  unicode: true
```

`embed-fonts` is a list of embedded fonts described by the following keys:

|key|Example|Description|
|---|-------|-----------|
|family|Monaco|Any string that you use to refer to the font in a family key later|
|fname|/System/Library/Fonts/Monaco.ttf|The location of a ttf file defining the font|
|unicode|true|A boolean indicating if you want to use the unicode version of the font. Set to false if a unicode version is not available|

All key are required