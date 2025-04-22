import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_tra_acf_unf(xs0, xs1, gen, genfunc ,mea , acfs1, burn_in, xbins):
    # plot trace, autocorrelation and unfolding results
    xs0_kept = xs0[burn_in:]
    xs1_kept = xs1[burn_in:]

    fig, ax = plt.subplots(2,2, figsize=(15,8))
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.2, hspace=0.2)

    # plot trace full
    ax[0,0].plot(xs1)
    ax[0,0].set_title('Trace, full')

    # plot autocorrelation, after burn-in
    ax[0,1].plot(acfs1)
    ax[0,1].set_xlabel('Lag (after burn-in)')
    ax[0,1].set_title('Autocorrelation')

    # plot true and measure distributions
    ax[1,0].hist(gen, bins=xbins, alpha=0.5, label='generated',density=True)
    ax[1,0].hist(mea, bins=xbins, alpha=0.5, label='observed',density=True)
    ax[1,0].plot(xbins, genfunc)
    ax[1,0].legend()
    
    # plot unfolded distributions, after burn-in
    ax[1,1].hist(gen, bins=xbins, alpha=0.5, label='generated',density=True)
    ax[1,1].hist(xs1_kept, bins=xbins, alpha=0.5, label=r'$\theta_{2}$ (after burn-in)',density=True)
    ax[1,1].plot(xbins, genfunc)
    ax[1,1].hist(xs0_kept, bins=xbins, alpha=0.5, label=r'$\theta_{1}$ (after burn-in)',density=True)
    ax[1,1].hist(mea, bins=xbins, alpha=0.5, label=r'$\theta_{0}$',density=True)
#    ax[1,0].plot(mh.ebins, kde(mh.ebins), 'r-', label='measurement PDF')
    ax[1,1].legend()

    
    


    