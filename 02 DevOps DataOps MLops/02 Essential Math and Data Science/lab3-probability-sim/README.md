

## Tasks

A.  Simulate a career earnings vs investor portfolio

1.  Run the `./startup.py` simulator and explore how each command works.

```bash
Usage: startup_game.py [OPTIONS] COMMAND [ARGS]...

  Startup Game Simulator

Options:
  --help  Show this message and exit.

Commands:
  sanity             Sanity test the simulation with a small number of...
  simulate           Simulate a startup career
  simulate_multiple  Simulate a startup career for multiple people
  vcportfolio        Simulate a venture capitalist investing in a...
```

2.  Create your own VC portfolio using `vcportfolio` and startup career using `simulate_multiple`.
* Reflection question:  What did you learn about the payoff for a regular employee vs. an investor?  
```
In the simulation, investing provides a greate payoff, but needs capital to be able to invest in the first place.

```
* Reflection question:  Why are simulations important first modeling steps?
```
Simulations are useful in providing some basic feedbacks for the model being used. 
They are only basic level, as the simulation might not have correct assumptions, or has drifted from the source data.
```
B. Determine if roulette wheels have patterns that a simulation can determine by running the following command

`./roulette.py spin --count 10 --color red --bet 1`

* Reflection question:  Is it is wise to bet a large bet on red if you see the roulette wheel hit 10 black numbers in a row?
```
No. While the chances may seem higher since so many blacks have been in a row, there is no difference in the chance of black vs red in the next spin as the number of positions haven't changed (there are still the same number of red and black positions).
```
* Reflection question:  Is there any behavior you could add to the roulette simulator that would improve it?  If so do it and build a portfolio project that shows your enhancement.
```
Adding a randomised seed could change the probabilities in the sampling function.
Other than that, I don't know enough about roulette to think of any improvements here.
```


### References

* [Coursera-MLOps-C2-lab3-probability-simulations](https://github.com/nogibjj/Coursera-MLOps-C2-lab3-probability-simulations)
