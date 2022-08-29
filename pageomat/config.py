def config_page_attribute(config, page, key, default_value):
    if key in page:
        return page[key]
    elif "defaults" in config and key in config["defaults"]:
        return config["defaults"][key]
    else:
        return default_value
