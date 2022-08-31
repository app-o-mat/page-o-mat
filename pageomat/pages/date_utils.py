from datetime import datetime


def format_day_of_year(year, day_of_year, date_format, vars):
    doy = day_of_year
    if type(day_of_year) is str:
        try:
            doy = eval(day_of_year, vars, {})
        except BaseException:
            print("Error evaluating: " + day_of_year)
            print("with variables " + str(vars))
            raise
    date = datetime.strptime(str(year) + "-" + str(doy), "%Y-%j")
    return datetime.strftime(date, date_format)


def date_replace(title, key, year, day_of_year, date_format, vars):
    date_str = format_day_of_year(year, day_of_year, date_format, vars)
    return title.replace("$" + key + "$", date_str)
