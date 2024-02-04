def parse_unknown_args(unknown_args, scope = {}):
    """
    parse_unknown_args([10, 30, "--a", "10", 40, "--a", 20, "--b", "--a", "--a", 30])
    --> {'a': ['10', 20, None, 30], 'b': None}
    """
    import argparse

    unknown_params = {}
    nargs = len(unknown_args)
    for idx in range(nargs):
        item  = unknown_args[idx]
        if type(item) is str and (item.startswith("--") or item.startswith("-")):
            item = item[2:] if item.startswith("--") else item[1:]
            item = item.replace("-", "_")
            value = unknown_args[idx + 1] if idx + 1 < nargs else None
            if type(value) is str and (value.startswith("--") or value.startswith("-")): value = None
            try:
                if str.isnumeric(value): value = eval(value)
                if value.lower() in ['true', 'false', 'yes', 'no']: value = eval(value)
            except:
                pass
            if unknown_params.get(item) is None:
                unknown_params[item] = value
            elif type(unknown_params[item]) is not list:
                unknown_params[item] = [unknown_params[item], value]
            else:
                unknown_params[item].append(value)
        # if
    # for
    return argparse.Namespace(**unknown_params)
    pass # parse_unknown_args