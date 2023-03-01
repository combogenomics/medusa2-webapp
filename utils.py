#!/usr/bin/env python

def generate_time_hash(data):
    '''Return a sha256 hash
    
    Salted hash including the client data
    and date/time
    '''
    import hashlib
    from datetime import datetime
    from time import strftime
    
    return hashlib.sha256("salegrosso" +
             data +
             datetime.now().strftime("%Y%m%d%H%M%S%f")).hexdigest()

def generate_hash(data):
    '''Return a sha256 hash
    
    Salted hash including only the client data
    '''
    import hashlib
    
    return hashlib.sha256("salegrosso" +
             data).hexdigest()

# TODO: add credits
def N50(numlist):
    """
    Abstract: Returns the N50 value of the passed list of numbers.
    Usage:    N50(numlist)

    Based on the Broad Institute definition:
    https://www.broad.harvard.edu/crd/wiki/index.php/N50
    """
    numlist.sort()
    newlist = []
    for x in numlist :
        newlist += [x]*x
        # take the mean of the two middle elements af there are an even number
        # of elements.  otherwise, take the middle element
    if len(newlist) % 2 == 0:
        medianpos = len(newlist)/2
        return float(newlist[medianpos] + newlist[medianpos-1]) /2
    else:
        medianpos = len(newlist)/2
        return newlist[medianpos]

def check_first_line(line):
    if line[0] != ">":
        return 0
    if line[0] == ">" and line[1] == "\n":
        return 1
    else:
        return 2

def check_empty_sequence(line1, line2):
    if line1[0] == ">" and line2[0] == ">":
        return 1
    if line1[0] == ">":
        #getId(line1)
        return 0
    if line2[0] == ">":
        #getId(line2)
        return 0

def check_sequence(line):  # allowed characters: ATCGN
   good_sequency=0;
   if line[0] != ">":
    for c in line:
            if c.upper()=="A" or c.upper()=="T" or c.upper()=="C" or c.upper()== "G" or c.upper()=="N" or c =="\n":
                continue
            else:
                return 1
   if good_sequency ==0:
    return 0