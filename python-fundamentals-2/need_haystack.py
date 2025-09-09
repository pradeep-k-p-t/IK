def substring(needle : str,haystack :str): 
    # find substring 
    len_needle = len(needle)
    # Case 2 : what if needle is empty 
    if len_needle == 0:
        return len_needle
    # Case 1 : haystack is too small or it is none 
    if haystack == None or len(haystack) < needle : 
        return -1 
    else: 
        
        for i in range(ml-nl+1):
            if haystack[i:(i+nl)] == needle:
                return i
        return -1