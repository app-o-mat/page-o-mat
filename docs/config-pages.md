# Page-o-Mat Configuration: page keys

This document describes keys that can be used in a page object. Each key can appear in a page defined in a `pages` list or in the `defaults` top-level key.

For example, a page can have a title, so you could have a default title like this

```yaml
page-size: A5
defaults:
- title: Default Title

pages:
- type: simple
- type: simple
  title: Override Title
```

The first page will have the "Default Title", and the second page will have the "Override Title".

## Page keys
|key|Type|Description|
|---|-------|-----------|
|type|`Enumeration` simple \| horizontal-sections|The page template|
|count|`Int`|Repeat this page block `count` times.|
|pages|`list of objects`|A list of sub-pages for this page. Use any of the keys on this page to form sub-page objects|
|variants|`list of strings`|Will make this page object repeat for each variant, setting `$variant$` to the current variant string.|


### Date keys
|key|Type|Description|
|---|-------|-----------|
|year|`Int`|Year to use in any date math -- see [day-of-year](config-day-of-year.md) keys|
|date-format|`string` in date format form|e.g. `"%-d %b"`. To format dates in page titles. See [strftime docs](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)|
|day-of-year|`Int` or `string`|Used to set `$date$` that can be used in the title. See [day-of-year](config-day-of-year.md)|
|start-year|`Int`|Year to use in any date math for `$start-date$` -- see [day-of-year](config-day-of-year.md) keys|
|start-day-of-year|`Int` or `string`|Used to set `$start-date$` that can be used in the title. See [day-of-year](config-day-of-year.md)|
|end-year|`Int`|Year to use in any date math for `$end-date$` -- see [day-of-year](config-day-of-year.md) keys|
|end-day-of-year|`Int` or `string`|Used to set `$end-date$` that can be used in the title. See [day-of-year](config-day-of-year.md)|

### Drawing keys

The units of the page are either millimeters (for A5, A4, or A3) or inches (for Letter or Legal)

|key|Type|Description|
|---|-------|-----------|
|drawing|`list of objects`|A list of drawing objects. See [drawing keys](config-drawing.md)|
|paper|`object`|The type of paper. Use [paper sub-keys](config-paper.md).|
|grid-snap|`number`|Used when drawing lines on top of the paper. If you match your paper, then lines will be on the same grid as the paper.|
|line-color|`hex color` (e.g. `"#333333"`)|Color for drawing lines|
|line-width|`number`|Width of the line in page units|

### Title and Footer keys

The units of the page are either millimeters (for A5, A4, or A3) or inches (for Letter or Legal)

|key|Type|Description|
|---|-------|-----------|
|top-margin|`number`|The margin to reserve at the top of the page (where titles start)|
|title|`string`|A string to use as the title. Use `$variant$` if you want the current page variant in the string or `$date$` if you want the date|
|page-link|`number`|The page number to link the title to in the PDF. This is 1-based. Can use a string that evaluates to a number using indices. NOTE: All indices are 0-based, including page number (`p`), so you might need to add one.|
|title-font|`object`|Define a font to use for page titles. See [font keys](config-font.md)|
|title-color|`hex color` (e.g. `"#cc00dd"`)|A color to use for the title|
|title-align|`Enumeration` Left \| Center \| Right|Used to align the title horizontally|
|show-title|`Bool`|Whether or not to show the title on this page. Can be a string expression of the indices that resolves to a boolean|
|subtitle|`string`|A string to use as the subtitle. Use `$variant$` if you want the current page variant in the string or `$date$` if you want the date|
|subtitle-font|`object`|Define a font to use for page subtitles. See [font keys](config-font.md)|
|subtitle-color|`hex color` (e.g. `"#cc00dd"`)|A color to use for the subtitle|
|subtitle-align|`Enumeration` Left \| Center \| Right|Used to align the subtitle horizontally|
|show-subtitle|`Bool`|Whether or not to show the subtitle on this page. Can be a string expression of the indices that resolves to a boolean|
|footer|`string`|A string to use as a page footer. Use `$page$` to get the page number|
|footer-font|`object`|See [font](config-font.md)|
|footer-color|`hex color` (e.g. `"#333333"`)|Footer color. A 3 or 6 hex digit RGB color|
|footer-align|`Enumeration` Left \| Center \| Right|Used to align the title horizontally|
|footer-offset|`number`|Distance from the bottom to put the footer baseline|


### Section keys

The units of the page are either millimeters (for A5, A4, or A3) or inches (for Letter or Legal)

|key|Type|Description|
|---|-------|-----------|
|section-count|`Int`|The number of sections on the page|
|section-left-margin|`number`|The left offset used when drawing sections|
|section-top-margin|`number`|The top offset used when drawing sections|
|section-title|`string`|The title for the section. Use `$section-start-date$` or `$section-end-date$` to substitute dates into the string (which were calculated from section day-of-year keys)|
|section-title-font|`object`|Define a font to use for section titles. See [font keys](config-font.md)|
|section-title-color|`hex color` (e.g. `"#333333"`)|Used to draw the section title|
|section-date-format|`string` in date format form|e.g. `"%-d %b"`. To format dates in section titles. See [strftime docs](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)|
|section-start-day-of-year|`Int` or `string`|Day of year that a section begins. See [day-of-year](config-day-of-year.md)|
|section-end-day-of-year|`Int` or `string`|Day of year that a section ends. See [day-of-year](config-day-of-year.md)|
|section-start-year|`Int` or `string`|Year to use in any date math -- see [day-of-year](config-day-of-year.md) keys|
|section-end-year|`Int` or `string`|Year to use in any date math -- see [day-of-year](config-day-of-year.md) keys|
|section-page-link|`number`|The page number to link the section title to in the PDF. This is 1-based. Can use a string that evaluates to a number using indices. NOTE: All indices are 0-based, including page number (`p`), so you might need to add one.|