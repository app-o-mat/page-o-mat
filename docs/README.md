# Page-o-Mat Documentation

Page-o-Mat is a command-line utility that generates a PDF from a YAML configuration.
It is intended to be used to create journals, so it supports a few blank page styles
and simple templates. It also supports a way to do date math based on page indices
so that you can put start and end dates on pages and sections within pages in whatever
date format you wish.

## Installation

1. Clone this repo
1. Install dependencies

   `pip install -r requirements.txt`
1. Run Page-o-Mat with a config

   `python pageomat/main.py --config config/daily.yaml --output daily.pdf`

1. daily.pdf is a sample 2023 Daily Journal PDF. It has 365 pages, each with the date on top.

## Configuration File Specification

The Page-o-Mat configuration file is a YAML formatted file with the following top level keys:

|key|Type|Description|
|---|-------|-----------|
|page-size|`Enumeration` A5 \| A4 \| A3 \| Letter \| Legal|The size of the page. This also sets the page units to either millimeters (For A sizes) or inches (For Legal or Letter)|
|pdf-title|`string`|Used in PDF meta-data|
|pdf-author|`string`|Used in PDF meta-data|
|defaults|`list of objects`|Defaults for pages. See [pages](config-pages.md).
|pages|`list of objects`|A list of page block objects. See [pages](config-pages.md).
|embed-fonts|`list of objects`|Used to embed fonts in the PDF (see [embed-fonts](config-embed-fonts.md))|

When you set **page-size**, you are also setting the units for all metrics. A5, A4, and A3 use millimeters. Letter and Legal use inches.

Each item in the **pages** list defines a block of pages. Page keys that are not specified in a page object use the value defined in the **defaults** list.

A minimal configuration would be:

```yaml
---
page-size: A5

pages:
- type: simple
  count: 2
```

This would generate a 2-page PDF at A5 size. Each page would be blank

To make a 100 page journal with a dot grid, use

```yaml
---
page-size: A5
defaults:
  paper:
    type: dot
    spacing: 5
    dot-size: 0.5
    color: "#aaa"

pages:
- type: simple
  count: 100
```

There are more sample configurations in the config folder.