# Journal Generator

Generates a daily journal PDF from a specification.

This is a work in progress. Currently, it is intended to generate the 2023 daily journal described in https://loufranco.com/blog/recurring-journals.

There is a configuration file that allows some customization, but the
page types are limited.

# Setup

There is a requirements file to install dependencies. Using `pip`, you can run

```bash
$ pip -r requirements.txt
```

# Usage

```bash
$ python src/jg.py -h
usage: jg.py [-h] --config CONFIG --output OUTPUT

Runs Journal Generator

options:
  -h, --help       show this help message and exit
  --config CONFIG  name of the journal config file
  --output OUTPUT  name of the pdf file

$ python src/jg.py --config config/2023-recurring-journal.json --output 2023.pdf
```

Sample configuration files can be found in the `config` folder.