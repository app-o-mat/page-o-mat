# Page-o-Mat Configuration: day-of-year keys

All `day_of_year` keys could either be an integer or a string.

If it's an integer, then it is the day of the year where 1 is January 1st, 2 is January 2nd, and so on.

If it's a string, then it's an expression that would calculate an integer day of year given the current indices while generating the page.

To understand the indices, consider this page block:

```yaml
- count: 2 # outer_count
  pages:
  - count: 4 # inner_count
    type: horizontal-sections
    section-count: 2
    variants:
    - Monday
    - Tuesday
    - Wednesday
    - Thursday
    - Friday
    - Saturday
    - Sunday
```

You can think of it as defining a loop like this (pseudo-code):

```python
for c0 in 0..outer_count:
  for v in 0..variant_count:
    for c1 in 0..inner_count:
      p = current_page_number()
      for s in 0..section_count:
        date = calc_date(day_of_year, year, indices={p:p, c: [c0, c1], v:v, s:s})
        draw_page_section(date)
```

Where `day_of_year` is the expression in your key

All indices are 0-based
- p is the current page number
- c is a list of "count" indices (c[0] is the top level parent)
- s is a section index
- v is a variant index