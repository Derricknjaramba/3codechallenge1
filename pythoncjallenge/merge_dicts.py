# merge_dicts.py

def merge_dicts(dict1, dict2):
    # Merges two dictionaries, summing the values for common keys
    merged = dict1.copy()  # Create a copy of the first dictionary
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  # Sum values for common keys
        else:
            merged[key] = value  # Add new key-value pairs
    return merged
