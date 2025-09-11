
def find_winner(votes):
    """
    Args:
     votes(list_str)
    Returns:
     str
    """
    # Write your code here.
    candidates = {}
    output = set()
    max_votes = 0 

    if votes == None or len(votes) ==0: 
        return []
    
    for name in votes: 
        if name in candidates:
           candidates[name] +=1
        else:
            candidates[name] = 1
   
   
    for key,val in candidates.items(): 
       if val > max_votes: 
           max_votes = val
           output = {key}
       if candidates[key] >= max_votes: 
           output.add(key)
           max_votes = val
    output = list(output)
    return output[0]

votes = ["sam", "john", "jamie", "sam"]
print(find_winner(votes))