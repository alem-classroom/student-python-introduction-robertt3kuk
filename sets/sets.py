

def size_of_set(set):
    # return size of set

    return len(set)


def is_elem_in_set(set, elem):
    # return true if elem exists in set, false otherwise
    check = list(set)
    if check.count(elem) > 0:
        return True
    else:
        return False


def are_sets_equal(first_set, second_set):
    # return true if sets have the same elements inside, otherwise false
    if first_set == second_set:
        return True
    else:
        return False


def add_elem_to_set(set, elem):
    # add elem to the set if elem does not exist in set, and return the se
    # if elem exists in set, return set
    check = list(set)
    if check.count(elem) > 0:
        return set
    else:
        set.add(elem)
        return set


def remove_elem_if_exists(set, elem):
    # remove elem from set if it exists, and return the set
    set.pop()
    return set


def delete_first_element(set):
    # delete first elemenent of set
    set.pop(0)
    return set
