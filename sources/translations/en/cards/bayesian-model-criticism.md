# Why posterior updating cannot replace model criticism

If data can only be explained with a straight line, adjusting the slope and intercept may find a better line but will not automatically produce a curve. This illustration captures the distinction emphasized by Gelman and Shalizi: choosing parameters within a model and discovering that the model is inadequate are different tasks.

## Posterior updating reweights existing explanations

Let D be the observed data and θ the model parameters. Bayesian updating combines the prior probabilities of parameters with how well they account for the data:

```math
p(\theta\mid D)\propto p(D\mid\theta)\,p(\theta).
```

The prior p(θ) describes beliefs before observing the data. The likelihood p(D|θ) measures how probable the data are under θ. The posterior p(θ|D) describes beliefs afterward. The proportionality symbol means that a normalizing constant is needed to make the total probability one.

This comparison stays within the specified model. If an important variable or relationship is missing, more data may concentrate the posterior around the best-fitting parameters without testing whether the model family is adequate. In the line example, greater certainty about a slope does not remove a curved pattern in the data.

## Predictive checks look for what the model misses

Model criticism asks what features the data should exhibit if the current model were adequate. It then compares predictions with observations to find systematic discrepancies. For example, prediction errors that vary systematically with the input can suggest a missing relationship rather than merely imprecisely estimated parameters.

Researchers can respond by choosing different variables, changing the functional form, or revising assumptions about data generation, then fitting and checking again. Posterior computation learns within the current model; predictive checks and revisions change the explanations available for subsequent learning.

## Why evidence selection matters for self-improvement

[Memento 3](memento-3.md) writes experience into revisable rules and encounters a related distinction: new feedback may require adjusting an existing rule or rewriting the rule itself.

Which errors a check can reveal also depends on the available data. Two models may predict past experience equally well while disagreeing about actions never tried. A system that always acts according to one model may never encounter evidence that distinguishes them. Model revision therefore requires both using existing counterexamples and taking actions that can expose new ones.

## Source and reading locations

Gelman and Shalizi, *Philosophy and the practice of Bayesian statistics*, published in 2013. This note uses the [authors' arXiv v3 full text](https://arxiv.org/html/1006.3868v3), particularly §2, §4.1, and §4.3. The article is a methodological analysis of statistical modeling.
