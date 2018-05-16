def prime_mover(plist, hist, growth):
    """Project exponentially-growing prime mover"""
    for i in range(hist,len(plist)):
        plist[i] = plist[i-1] * (1 + growth)
    return plist

def secondary_mover(slist, plist, hist, ratio):
    """Project secondary mover as a ratio against a primary mover"""
    for i in range(hist, len(slist)):
        slist[i] = plist[i] * ratio
    return slist

def summary_line(smlist, *args):
    """Sum up *args to produce a summary line item"""
    for arg in args:
        smlist += arg
    return smlist
