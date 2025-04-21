# MCMC-sampling
 Markov Chain Monte Carlo (MCMC) methods are sampling algorithms that exploit the properties of Markov Chain, a sequence of serially correlated random variables { X }, to obtain random samples from a probability distribution f(x). If a Markov chain is irreducible and aperiodic, then the Markov chain will converge to its unique stationary distribution, regardless of the initial state. The equilibrium distribution from draws of Markov Chain approximates the target probability distribution if the so-called detailed balance condition on the Markov process is met with respect to f(x).

### Properties of Markov Chain 
- Definition: The probability of current state transitioning to a new state depend only on the current state, \
  i.e. P(X<sub>t+1</sub>=x|X<sub>t</sub>=x<sub>t</sub>) = P(X<sub>t+1</sub>=x|X<sub>0</sub>=x<sub>0</sub>,X<sub>1</sub>=x<sub>1</sub>, $\cdots$ , X<sub>t</sub>=x<sub>t</sub>), where x<sub>i</sub>'s are observed states of random variables X<sub>i</sub>'s.
- As $n$ becomes larger, two observations of states X<sub>t</sub> and X<sub>t+n</sub> become closer to being independent of each other.
- As $t$ becomes larger, the sequence { X<sub>t</sub> } converges to the target distribution f(x)

### Detailed balance contidion
A Markov chain satisfies detailed balance with respect to a stationary distribution f(x) if \
  P(x<sub>t+1</sub>|x<sub>t</sub>) f(x<sub>t</sub>) = P(x<sub>t</sub>|x<sub>t+1</sub>) f(x<sub>t+1</sub>). \
This equation means that the probability of observing x<sub>t</sub> first and then x<sub>t+1</sub> is equal to the probability of observerving x<sub>t+1</sub> first and then x<sub>t</sub>. For this reason, if this equality holds, the Markov chain is said to be reversible with respect to a stationaly distribution f(x).


### Metropolis-Hastings algorithm
Metropolis-Hastings (MH) algorithm is one of the most widely used MCMC sampling method. Following steps are taken to generate samples.

1. 



### Use cases
Most common use cases for the methods are: 
 
$\bullet$ Sampling from complex and high dimensional distributions, e.g numerical integration of analytically intractable functions \
$\bullet$ Bayesian inference, e.g. exploration of posterior distributions, uncertainty quantification

Included example in this project is the Bayesian unfolding, where true distributions of observables are reconstructed from distorted ones in measurement processes. 


