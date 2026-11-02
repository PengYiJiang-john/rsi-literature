# Outside the Echo Chamber: optimizing performance after deployment feedback

A model can stop changing after repeated retraining on the data it induces, even though a better deployment remains possible. Miller, Perdomo, and Zrnic first learn how the environment responds to a model, then incorporate that response into optimization.

## Why a stable model can still be suboptimal

In the [performative prediction](performative-prediction.md) setting, θ denotes the deployed parameters, D(θ) the resulting data distribution, and ℓ(z; θ) the model's loss on a sample z. Performative risk is

```math
\mathrm{PR}(\theta)=\mathbb E_{z\sim D(\theta)}[\ell(z;\theta)].
```

Changing θ changes both the loss calculation and the source of data. Repeated retraining optimizes only the first part: each round holds the existing distribution fixed and finds the best parameters for it. At a fixed point, the current model is best for the current data, but optimization may have missed the benefit of inducing different data with another model.

The paper proves that a stable point can have substantially higher performative risk than the optimum. Even if the loss is convex in the parameters, PR need not be convex because D(θ) changes too. The authors impose structure on the distributional response to analyze the risk and develop optimization methods.

## Learn the response, then optimize deployment

In settings such as location families, the change in data can be described by a shift in the distribution's location. The authors deploy models, collect data, estimate how the parameters move the distribution, and use that estimate to optimize performative risk. Deployment thus supplies information about environmental responses for the next decision.

Experiments use synthetic linear regression with deployment effects and a credit-scoring simulator in which applicants adjust manipulable features. The authors compare the two-stage method with derivative-free optimization and stochastic-gradient methods with different update frequencies, tracking risk against the number of samples collected. The two-stage method optimizes performative risk more effectively in these settings. The experiments also include stronger feedback outside the regime covered by the theoretical guarantees.

## How to leave the echo chamber

Here, the “echo chamber” arises when a model repeatedly uses data it causes without accounting for how it causes those data to change. Estimating the environmental response lets optimization consider the consequences of a different deployment.

[Berk–Nash](berk-nash.md) examines which beliefs can support an action; this paper examines whether optimization accounts for an action's effect on future data. For RSI, the latter question extends the evaluation of a modification to the feedback it subsequently causes.

## Source and reading guide

Miller, Perdomo, and Zrnic, 2021, *Outside the Echo Chamber: Optimizing the Performative Risk*, ICML. [Paper page](https://proceedings.mlr.press/v139/miller21a.html) and [published PDF](https://proceedings.mlr.press/v139/miller21a/miller21a.pdf).

See §1.1 for the distinction between stability and optimality; §§3–5 and Figures 1–2 for theory, algorithms, and experiments.
