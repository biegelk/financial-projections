def prime_mover(plist, hist, growth):
    """Project exponentially-growing prime mover"""
    for i in range(int(hist),len(plist)):
        plist[i] = plist[i-1] * (1 + growth)
    return plist

def secondary_mover(slist, plist, hist, ratio):
    """Project secondary mover as a ratio against a primary mover"""
    for i in range(hist, len(slist)):
        slist[i] = plist[i] * ratio
    return slist

def summary_line(smlist, *args):
    """Sum up *args to produce a summary line item"""
    smlist = 0
    for arg in args:
        smlist += arg
    return smlist

def metric_ratio(rlist, nlist, dlist):
    """Compute a ratio of two line items"""
    for i in range(len(nlist)):
        rlist[i] = float(nlist[i]) / float(dlist[i])
    return rlist
