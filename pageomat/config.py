def config_page_attribute(config, page, key, default_value):
    if key in page:
        return page[key]
    elif "defaults" in config and key in config["defaults"]:
        return config["defaults"][key]
    else:
        return default_value


def config_attribute(config, key, default_value):
    if key in config:
        return config[key]
    else:
        return default_value


def eval_value(value, indices):
    if type(value) is str:
        vars = {"__builtins__": None}
        if indices is not None:
            vars.update(indices)
        value = eval(value, vars)

    return value


def eval_value_with_key(config, page, indices, key, default_value=None):
    value = config_page_attribute(page, config, key, default_value=default_value)
    return eval_value(value, indices)
