# MCMC-sampling
 Markov Chain Monte Carlo (MCMC) methods are sampling algorithms that exploit the properties of Markov Chain, a sequence of serially correlated random variables { X }, to obtain random samples from a probability distribution f(x). If a Markov chain is irreducible (ergodic) and aperiodic, then the Markov chain will converge to its _unique stationary_ distribution, _regardless_ of the initial state. If the so-called _detailed balance_ condition on this class of Markov process is met with respect to the stationay distribution, then the draws from such a Markov Chain will asymptotically reach an equilibrium distribution that approximates the target probability distribution f(x). 

### Properties of Markov Chain 
- By definition: The probability of current state transitioning to a new state depend only on the current state, \
  i.e. P(X<sub>t+1</sub>=x|X<sub>t</sub>=x<sub>t</sub>) = P(X<sub>t+1</sub>=x|X<sub>0</sub>=x<sub>0</sub>,X<sub>1</sub>=x<sub>1</sub>, $\cdots$ , X<sub>t</sub>=x<sub>t</sub>), where x<sub>i</sub>'s are observed states of random variables X<sub>i</sub>'s.
- As $n$ becomes larger, two observations of states X<sub>t</sub> and X<sub>t+n</sub> become closer to being independent of each other.
- As $t$ becomes larger, the sequence { X<sub>t</sub> } converges to the target distribution f(x)

### Detailed balance contidion
A Markov chain is said to satisfy detailed balance (or to be reversible) with respect to a probability distribution f(x) if \
  **P(x<sub>t+1</sub>|x<sub>t</sub>) f(x<sub>t</sub>) = P(x<sub>t</sub>|x<sub>t+1</sub>) f(x<sub>t+1</sub>)**. \
This equation says that the probability of observing x<sub>t</sub> first and then x<sub>t+1</sub> is equal to the probability of observerving x<sub>t+1</sub> first and then x<sub>t</sub>. If this equality holds, it can be shown that f(x) is a stationaly distribution of the Markov chain : 
$\sum$<sub>x<sub>t</sub></sub> P(x<sub>t+1</sub>|x<sub>t</sub>) f(x<sub>t</sub>) = $\sum$<sub>x<sub>t</sub></sub> P(x<sub>t</sub>|x<sub>t+1</sub>) f(x<sub>t+1</sub>) \
= f(x<sub>t+1</sub>) $\sum$<sub>x<sub>t</sub></sub> P(x<sub>t</sub>|x<sub>t+1</sub>) = f(x<sub>t+1</sub>).
The condition that a distribution is stationary requires a zero net flow on each state _globally_, while detailed balance imposes much stronger condition of _locally_ balanced flow between any states.


### Metropolis-Hastings algorithm
Metropolis-Hastings (MH) algorithm is one of the most widely used MCMC sampling method. Following steps are taken to generate samples.

1. 



### Use cases
Most common use cases for the methods are: 
 
$\bullet$ Sampling from complex and high dimensional distributions, e.g numerical integration of analytically intractable functions \
$\bullet$ Bayesian inference, e.g. exploration of posterior distributions, uncertainty quantification

Included example in this project is the Bayesian unfolding, where true distributions of observables are reconstructed from distorted ones in measurement processes. 


