"""autocorrelation.py: methods for computing autocorrelation."""

__author__      = "Sookhyun Lee"
__version__ = "1.0.0"
__email__ = "dr.sookhyun.lee@gmail.com"

import numpy
import matplotlib.pyplot as plt

def autocorr_np_corrcoef(x,lags):
    '''numpy.corrcoef, (incorrect) mean/variance change with lags'''

    corr=[1. if l==0 else numpy.corrcoef(x[l:],x[:-l])[0][1] for l in lags]
    return numpy.array(corr)

def autocorr_man(x,lags):
    '''manualy compute'''

    mean=numpy.mean(x)
    var=numpy.var(x)
    xp=x-mean
    corr=[1. if l==0 else numpy.sum(xp[l:]*xp[:-l])/len(x)/var for l in lags]

    return numpy.array(corr)

def autocorr_fft(x,lags):
    '''fft, pad 0s'''

    n=len(x)
    # pad 0s to 2n-1
    ext_size=2*n-1
    # nearest power of 2
    fsize=2**numpy.ceil(numpy.log2(ext_size)).astype('int')

    xp=x-numpy.mean(x)
    var=numpy.var(x)

    # do fft and ifft
    cf=numpy.fft.fft(xp,fsize)
    sf=cf.conjugate()*cf
    corr=numpy.fft.ifft(sf).real
    corr=corr/var/n

    return corr[:len(lags)]

def autocorr_fft_nopad(x,lags):
    '''fft, don't pad 0s, (incorrect) size mismatch for circular'''

    mean=x.mean()
    var=numpy.var(x)
    xp=x-mean

    cf=numpy.fft.fft(xp)
    sf=cf.conjugate()*cf
    corr=numpy.fft.ifft(sf).real/var/len(x)

    return corr[:len(lags)]

def autocorr_np_correlate(x,lags):
    '''numpy.correlate'''
    mean=x.mean()
    var=numpy.var(x)
    xp=x-mean
    corr=numpy.correlate(xp,xp,'full')[len(x)-1:]/var/len(x)

    return corr[:len(lags)]


if __name__=='__main__':
    '''
    To run in Jupyter Notebook, 
    %run autocorrelation.py

    Inspired by
    https://stackoverflow.com/questions/643699/how-can-i-use-numpy-correlate-to-do-autocorrelation

    * Auto-correlation is discussed in two contexts: statistical vs. convolution in signal processing 
      - Statistical auto-correlation entails establishing a statistical relation of the time series 
        at a point of time to previous covariates. It is normalized into the interval [-1,1].
      - Convolution is typically used in signal processing for smoothing/filtering, where a convolving 
        window, e.g. Sine wave, slides over your signal, multiplying and summing up contributions from  
        each point as you go. In this context, FFT can be used to increase the computation speed. 
    * Make sure the mean and variance of original data are consistenly used in computing the auto-
      correlation.
      Counter example: autocorr_np_corrcoef   
    * Standardizing data prior to computing auto-correlation is useful in that the resulting correlation 
      automatically falls within the range of -1 and 1, making the interpretation more straightforward.
      Also, it is easier to determine the statistical significance of autocorrelation, as it removes the 
      influence of scale. Methods here do return auto-correlations for standardized data. 
    * Padding zero's for FFT  
      https://dsp.stackexchange.com/questions/54924/autocorrelation-numpy-versus-fft

    '''
    
    y=[30,28,26,24,22,24,26,28,30,32,30,28,26,24,22,24,26,28,30,32,30,\
            28,26,24,22,24,26,28,30,32,30]
    y=numpy.array(y).astype('float')

    lags=range(15)
    fig,ax=plt.subplots()

    for method_i, label_i in zip([autocorr_np_corrcoef, autocorr_man, autocorr_fft, autocorr_fft_nopad,
        autocorr_np_correlate], ['np.corrcoef (x)', 'manual', 'fft, pad 0s', 'fft, no padding (x)',
        'np.correlate']):

        c_i=method_i(y,lags)
        print(label_i)
        print(c_i)
        ax.plot(lags,c_i,label=label_i)

    ax.set_xlabel('lag')
    ax.set_ylabel('correlation coefficient')
    ax.legend()
    plt.show()