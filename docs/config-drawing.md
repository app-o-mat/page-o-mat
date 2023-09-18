# Page-o-Mat Configuration: page drawing keys

This document describes keys that can be used in a drawing object. Each key can appear in a drawing object defined in a `drawing` list in a page.

For example, a page can have a drawing like this:

```yaml
pages:
- type: simple
  drawing:
    - type: rect
      pos: {x: 0, y: 0}
      size: {w: 20, h: 20}
      fill: "#FDD7A8"
    - type: circle
      pos: {x: 5, y: 5}
      size: {w: 1, h: 1}
      fill: "#807A73"
```

Here are the values for the `type` key:

|type|Description|
|----|-----------|
|rect|A rectangle|
|circle|A circle|
|ellipse|An ellipse|
|line|A line|
|text|A block of text|
|qr|A QR code|

Keys for `rect`

|key|Type|Description|
|---|-------|-----------|
|pos|`object`|The position of the top-left corner of the rectangle. Uses an `x` and `y` key. E.g. `{x: 0, y: 0}`|
|size|`object`|The size of the rectangle. Uses a `w` and `h` key. E.g. `{w: 20, h: 20}`|
|stroke|`hex color` (e.g. `"#333333"`)|Color for the outline of the rectangle|
|fill|`hex color` (e.g. `"#333333"`)|Color for the inside of the rectangle|
|alpha|`number`|Opacity of the rectangle. 0 is transparent, 1 is opaque.|

Keys for `circle`

|key|Type|Description|
|---|-------|-----------|
|center|`object`|The position of the center of the circle. Uses an `x` and `y` key. E.g. `{x: 0, y: 0}`|
|radius|`number`|The radius of the circle|
|stroke|`hex color` (e.g. `"#333333"`)|Color for the outline of the rectangle|
|fill|`hex color` (e.g. `"#333333"`)|Color for the inside of the rectangle|
|alpha|`number`|Opacity of the rectangle. 0 is transparent, 1 is opaque.|

Keys for `ellipse`

|key|Type|Description|
|---|-------|-----------|
|pos|`object`|The position of the top-left corner of the ellipse. Uses an `x` and `y` key. E.g. `{x: 0, y: 0}`|
|size|`object`|The size of the ellipse. Uses a `w` and `h` key. E.g. `{w: 20, h: 20}`|
|stroke|`hex color` (e.g. `"#333333"`)|Color for the outline of the ellipse|
|fill|`hex color` (e.g. `"#333333"`)|Color for the inside of the ellipse|
|alpha|`number`|Opacity of the ellipse. 0 is transparent, 1 is opaque.|

Keys for `line`

|key|Type|Description|
|---|-------|-----------|
|start|`object`|The position of the start of the line. Uses an `x` and `y` key. E.g. `{x: 0, y: 0}`|
|end|`object`|The position of the end of the line. Uses an `x` and `y` key. E.g. `{x: 10, y: 10}`|
|color|`hex color` (e.g. `"#333333"`)|Color for the line|
|alpha|`number`|Opacity of the line. 0 is transparent, 1 is opaque.|

Keys for `text`

|key|Type|Description|
|---|-------|-----------|
|pos|`object`|The position of the top-left corner of the text. Uses an `x` and `y` key. E.g. `{x: 0, y: 0}`|
|size|`object`|The size of the box containing a line of text. E.g. `{w: 20, h: 20}`. The width will be used for wrapping and the height will be used for the line height.|
|text|`string`|The text to draw|
|color|`hex color` (e.g. `"#333333"`)|Color for the text|
|alpha|`number`|Opacity of the text. 0 is transparent, 1 is opaque.|
|align|`Enumeration` Left \| Center \| Right|Used to align the text horizontally|
|font|`object`|Define a font to use for the text. See [font keys](config-font.md)|

Keys for `qr`

|key|Type|Description|
|---|-------|-----------|
|pos|`object`|The position of the top-left corner of the QR code. Uses an `x` and `y` key. E.g. `{x: 0, y: 0}`|
|size|`object`|The size of the QR code. Uses a `w` and `h` key. E.g. `{w: 20, h: 20}`|
|text|`string`|The text to encode in the QR code|