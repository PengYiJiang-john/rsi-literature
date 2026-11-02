# Dual control and the learning value of actions

Consider pushing an object with unknown resistance. The force affects how far it moves, while the observed displacement helps reveal its resistance. One action changes both the physical state and what the controller knows. Dual control asks whether the cheapest action now might sacrifice an experiment that would be useful later.

## Why substituting an estimate is not enough

Klenske and Hennig study control over a finite horizon with unknown dynamics. The decision maker tracks the current physical state and a probability distribution over unknown parameters. An action changes the state; the resulting observation updates the parameter distribution. Both changes matter for the next decision.

A common simplification estimates the parameters and then controls the system as if those estimates were correct. This is certainty-equivalent control. It uses existing knowledge but does not account for how the current action might help future learning. Dual control includes that benefit: a slightly more costly action can be worthwhile if it resolves an important uncertainty and improves later actions.

Planning is difficult because the next observation is unknown. Each action can produce several observations, each leading to different beliefs and subsequent decisions. The paper makes this calculation tractable through a local second-order approximation of future costs around a precomputed reference trajectory.

## Testing when exploration is useful

The authors compare four controllers: one given the true dynamics, a certainty-equivalent controller, a controller with an exploration bonus, and an approximate dual controller. The simulations vary the timing and cost of exploration, the relevance of unknown parameters to later tasks, and how quickly knowledge becomes outdated.

Exploration can be delayed when it becomes cheaper later and the cost of waiting without that knowledge is small. A parameter that does not affect later actions warrants little exploration cost. Knowledge that soon becomes obsolete is less valuable to acquire early. The simulations show how approximate dual control uses these differences to choose its experiments.

## From information value to action selection

[Blackwell's comparison](blackwell-information.md) asks which decisions a given signal supports. Dual control makes signal acquisition part of the action: current knowledge determines what to try, and the result changes subsequent knowledge. [Information-directed sampling](information-directed-sampling.md) focuses exploration on the unknown identity of the best action.

The form of the dynamics model and the approximate planning method remain fixed. Beliefs and the actions chosen from them change.

## Source and reading locations

Edgar Klenske and Philipp Hennig (2016), *Dual Control for Approximate Bayesian Reinforcement Learning*, JMLR 17(127). [Paper page](https://jmlr.org/papers/v17/15-162.html); [full PDF](https://jmlr.org/papers/volume17/15-162/15-162.pdf).

Checked: §3.1, equation (7), §4, and §6.1–6.5; experimental comparisons in Figures 1 and 5–7 and Table 1.
