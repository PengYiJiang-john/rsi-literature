# Information-directed sampling to find the best action

A learner facing several options could investigate many unknowns, but only some affect which option is best. Russo and Van Roy's information-directed sampling focuses exploration on this question: how much immediate reward must the learner give up to obtain information about the optimal action?

## Each experiment has a cost and an information gain

Let A★ be the action with the highest expected reward in the unknown environment. Given the observations so far, the learner assigns probabilities to the possible identities of A★. These probabilities form its posterior distribution over the optimal action.

For a candidate action a, Δₜ(a) is the expected reward lost by choosing a instead of A★, or expected regret. The quantity gₜ(a) is the expected reduction in uncertainty about A★ after observing the feedback from a, measured by mutual information. Both use the history available before step t.

The algorithm may randomize its choice. If p(a) is the probability of choosing a, it minimizes the information ratio:

```math
\Psi_t(p)=
\frac{\left(\sum_a p(a)\Delta_t(a)\right)^2}
{\sum_a p(a)g_t(a)}.
```

The numerator is squared expected regret; the denominator is expected information gain. The optimization is over the whole distribution p. Mixing actions can improve this trade-off, so the procedure is not equivalent to scoring each action separately and choosing the lowest score.

## Why not resolve every uncertainty?

Imagine a highly uncertain environmental parameter whose value never changes which action is best. Learning more about it increases knowledge of the world but does not identify A★. Conversely, a simple observation can be valuable if it rules out a strong but incorrect contender for the best action.

The paper assumes a specified Bayesian environment model and a finite action set. The function mapping feedback to reward is known, and rewards are bounded; the environment's feedback distribution is unknown. Conditional on the environment, potential feedback is independent and identically distributed across rounds. Which feedback the learner actually observes still depends on its actions.

The theory connects cumulative regret to the information ratio and the initial uncertainty about the optimal action. A uniform bound on the ratio controls cumulative regret. Experiments on Bernoulli and linear bandits compare cumulative regret with upper-confidence-bound methods, Thompson sampling, and knowledge-gradient methods.

## Its place in the feedback process

[Dual control](dual-control.md) jointly considers present actions and future learning; information-directed sampling allocates exploration around the optimal action. Both infer within a specified environment model. Once informative feedback has been selected, the learner must still extract the relevant distinctions from it. [Usable information](usable-information.md) studies that next step.

## Source and reading locations

Daniel Russo and Benjamin Van Roy (2014), *Learning to Optimize via Information-Directed Sampling*, NeurIPS. [Published full PDF](https://papers.neurips.cc/paper/5463-learning-to-optimize-via-information-directed-sampling.pdf).

Checked: §2–4, equations (5)–(6), Proposition 2, and §6. The formula above expresses the information ratio over action distributions.
