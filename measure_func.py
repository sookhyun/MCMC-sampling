import numpy as np
import scipy.stats as stats

def gaus_homoscedastic(the, sft, res):
    # scale : sigma = f(x) resolution fn
    meas = stats.norm(loc=the + sft, scale=res).rvs()
    return meas

