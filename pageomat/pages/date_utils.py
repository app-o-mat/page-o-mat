from datetime import datetime


def eval_with_variables(value, vars):
    return_val = value
    if type(value) is str:
        try:
            return_val = eval(value, vars, {})
        except BaseException:
            print("Error evaluating: " + value)
            print("with variables " + str(vars))
            raise
    return return_val


def format_day_of_year(year, day_of_year, date_format, vars):
    try:
        doy = eval_with_variables(day_of_year, vars)
        y = eval_with_variables(year, vars)
        date = datetime.strptime(str(y) + "-" + str(doy), "%Y-%j")
        return datetime.strftime(date, date_format)
    except BaseException:
        print("Error formatting day of year: " + str(y) + " " + str(doy) + " " + str(date_format))
        print("day_of_year: " + str(day_of_year))
        print("year: " + str(year))
        print("with variables " + str(vars))
        raise


def date_replace(title, key, year, day_of_year, date_format, vars):
    date_str = format_day_of_year(year, day_of_year, date_format, vars)
    return title.replace("$" + key + "$", date_str)
