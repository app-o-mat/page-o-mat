# Page-o-Mat Journal Generator

Generates a journal PDF from a specification. Suitable for printing into a book.

This is a work in progress. Currently, it is intended to generate the 2023 daily journal described in https://loufranco.com/blog/recurring-journals.

There is a configuration file that allows some customization, but the
page types are limited.

# Documentation

[Full docs](docs)

# Setup

There is a requirements file to install dependencies. Using `pip`, you can run

```bash
$ pip -r requirements.txt
```

# Usage

```bash
$ python pageomat/main.py -h
usage: main.py [-h] --config CONFIG --output OUTPUT

Runs Page-o-Mat

options:
  -h, --help       show this help message and exit
  --config CONFIG  name of the journal YAML config file
  --output OUTPUT  name of the pdf file

$ python pageomat/main.py --config config/2023-recurring-journal.yaml --output 2023.pdf
```

Sample configuration files can be found in the `config` folder.