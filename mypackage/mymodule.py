def top_n(items, n):
    """
    Return the top n items in an array, in desc order.

    Args:
        items (array): list or array like object. 
        n (int): the number of items to return

    Return:
        array: top n items, in desc order.

    Ex:
        >>> top_n([1,3,2,4], 3)
        output: [4,3,2] 
    """

    if 0 < n < len(items):
        for i in range(n): # keep sorting untill we havethe top n items
            for j in range(len(items)-1-i):

                if items[j] > items[j+1]: # if this item is bigger than the next item
                    items[j], items[j+1] = items[j+1], items[j] # swap the two

        # get last two items
        top_n = items[-n:]

        # return in desc order
        return top_n[::-1]
    else:
        print(f"n must be between 0 and {len(items)-1}")
