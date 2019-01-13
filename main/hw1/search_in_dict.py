def search_in_dict(list, dict):
    result = set()
    for i in list:
        if (dict.get(i)): result.add(i)
    return result
