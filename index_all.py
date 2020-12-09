def index_all_ans(lst, val):
    """ Find all indices of a given value in the input list
    return a list of indices """
    retVal = list()
    # iterate through values
    for i in range(len(lst)):
        # compare to the value we want
        if lst[i] == val:
            retVal.append([i])
        # check if item is a list
        elif isinstance(lst[i], list):
            # iterate using recursion
            for idx in index_all_ans(lst[i], val):
                retVal.append([i]+idx)
    
    return retVal

