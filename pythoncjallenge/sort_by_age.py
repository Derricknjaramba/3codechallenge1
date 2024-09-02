# sort_by_age.py

def sort_by_age(lst):
    # Sorts a list of tuples by the age (second element) in ascending order
    return sorted(lst, key=lambda x: x[1])
