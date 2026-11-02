# Metareasoning: When Is More Computation Worthwhile?

A game-playing program has found a promising move. Should it simulate other moves before acting? Hay and colleagues formulate this as a decision problem: computation is valuable insofar as it improves the eventual action, after accounting for its cost.

## Treating computation as a decision

A simulation does not place a stone on the actual board. It supplies a result that updates the program’s assessment of candidate moves. The paper treats completed computations and their results as the metalevel state. The agent can choose another computation or stop and execute its current best action. The objective is the utility of the final action minus computational costs.

If a simulation is unlikely to change the choice, reducing uncertainty may offer little task value. If two promising actions remain difficult to distinguish, a computation that could change the choice is more valuable. Each computation also affects which later computations are worthwhile, so an optimal policy generally evaluates sequences of computations. A metalevel Markov decision process expresses this choice.

## Allocating computation in selection problems and Go

Solving the full metalevel problem is itself expensive. The authors develop approximations and heuristics, comparing allocations of simulation resources in selection problems and Go. Go offers a clear feedback setting: simulations follow known rules, and their outcomes help compare candidate moves. The problem is how to make better choices with a limited number of simulations.

The cost here is internal computation, distinct from the return forgone by actually trying an external action. Search and verification can therefore improve a decision before the external action is taken.

## From choosing computations to modifying programs

The [Gödel machine](godel-machine.md) extends the choice to whether a program should modify itself now or continue searching. It also allows changes to the program that searches for proofs. Both approaches evaluate whether further computation is worthwhile; the latter can additionally change how future computation is performed.

## Source and reading guide

Hay et al. (2012), *Selecting Computations: Theory and Applications*, UAI. See the definitions in §2 and the analyses and applications in §4–6.

[Publication](https://proceedings.mlr.press/r10/hay12a.html) · [Full text consulted](https://arxiv.org/html/1207.5879v1)
