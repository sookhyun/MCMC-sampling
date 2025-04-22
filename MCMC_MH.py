"""MH_sampling.py: Implementation of Metropolis-Hastings sampling algorithm."""

__author__      = "Sookhyun Lee"
__version__ = "1.0.1"
__email__ = "dr.sookhyun.lee@gmail.com"

import numpy as np
import scipy.stats as stats

class MH_sampling:    
    
    def __init__(self, X, ptX):
        self.X = X
        self.Xbegin = np.mean(X)-3*np.std(X) 
        self.Xend = np.mean(X)+3*np.std(X)
        self.cbins = np.linspace(self.Xbegin, self.Xend, num=200) 
        self.ebins = self.cbins
        self.ptX = ptX
        self.prior_pdf = None
        self.likelihood_fn = None
        self.marginal = None
        self.measurement_pdf = None
        self.measurement_eff = None
        self.integrate_effect = False # P(C) instead of P(C|E); Effect = Observed
        #if self.ptX == None:
        #    print(f'You have chosen to use your own posterior pdf. Available to define are:'
        #    f'\n prior_pdf \n likelihood_fn '
        #    f'\n measurement_pdf [if integrate_effect = True]')
                
    def ptX_custom(self, theta, Xobs):
        eps= 10**-40
    
        if self.integrate_effect == True:            
            # Target posterior given observations X ={X_i| i=0, ... ,n} : int dX_i [P(t|X_i)p(X_i)] = post(t) 
            # P(X_i|t) prior(t) / marginal_likelihood * p(X_i) = P(t|X_i)p(X_i) for a given observation X_i
            # Marginal likelihood : int dt P(X_i|t)p(t) 
            loglik_i = np.log(self.likelihood_fn(theta, self.ebins))
            logmarginal_i = self.marginal
            logeffect_i = np.log(self.measurement_pdf(self.ebins))
            posterior = np.sum(np.exp(loglik_i - logmarginal_i + logeffect_i))
            posterior *= (self.prior_pdf(theta)/self.measurement_eff(theta))
            return np.log(posterior)
            
        # Unnormalized posterior: log[P(X_1|t)...P(X_n|t)p(t)]   
        loglik = np.sum(np.log(self.likelihood_fn(theta,Xobs)+eps)) 
        logprior = np.log(self.prior_pdf(theta))
        
        return loglik + logprior 

    def compute_marginal(self):
        marg=np.array([self.likelihood_fn(ca, self.ebins)*self.prior_pdf(ca) for ca in self.cbins])
        marglik= np.log(np.sum(marg.T, axis=1))
        self.marginal = marglik
        
    
    def get_sample_Bayes(self, t0, q, qprob, nsample=1000):   
        if self.ptX == None:
            self.ptX = self.ptX_custom
            self.compute_marginal()
        t = t0
        ts = [t]
        logps =[]
        naccepted = 0        
        acceptance_rates = []
        
        for i in range(nsample):
            if i%1000 == 0 and nsample > 5000 :
                print('event ', i)
            while True:
                tnew = q(t) # proposal distribution
                if tnew > self.Xbegin and tnew < self.Xend :
                    break
            logp = self.ptX(t, self.X) # log p(t|X) log posterior probability
            logp_new = self.ptX(tnew, self.X)
        
            if logp_new > logp:
                ratio = 1 # A is always 1 for sysmetric q
            else:
                qr = 1 #qprob(t, tnew)/qprob(tnew, t) # 1 for Gaussian proposal
                ratio = np.exp(logp_new - logp) * qr
            A = min(1, ratio)
            
            if A > stats.uniform(0,1).rvs():
                t = tnew
                naccepted += 1

            logps.append(logp)
            ts.append(t)
            acceptance_rates.append(naccepted/(i+1))

        return ts, acceptance_rates, logps

def q_normal(x):
    # proposal based on Gaussian
    xnew = stats.norm(loc=x, scale=2).rvs()
    return xnew

def qprob_normal(x1, x2):
    # proposal probability q(x2|x1), based on Gaussian
    q = stats.norm(loc=x1, scale=2).pdf(x2)
    return q

def ptX_normal(theta, X):
    # returns the unnormalized log posterior for Bayesian inference
    loglik = np.sum(np.log(stats.norm(loc=theta, scale=1).pdf(X)))
    logprior = np.log(stats.norm(loc=0, scale=1).pdf(theta))    
    return loglik + logprior