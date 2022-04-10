def reverse_dict(dict):
    # swap keys and values wtthin dict and return dict
    dict = {value: key for key, value in dict.items()}
    return dict
